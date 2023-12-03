#include "los/ppm.hpp" // Inclusion du fichier d'en-tête ppm.hpp

#include <fstream>  // Inclusion pour la gestion des fichiers
#include <iostream> // Inclusion pour les entrées/sorties
#include <sstream>  // Inclusion pour les flux de chaînes
#include <string>   // Inclusion pour les chaînes de caractères

namespace los
{
    // Constructeur de la classe Heightmap avec largeur et hauteur spécifiées
    Heightmap::Heightmap(const uint32_t width, const uint32_t height) : m_width(width), m_height(height)
    {
        // Initialisation du vecteur de pixels avec des zéros
        m_pixels = std::vector<uint8_t>(m_width * m_height, 0u);
    }

    // Constructeur de la classe Heightmap à partir d'un fichier PPM
    Heightmap::Heightmap(const char *const name) : m_width(0), m_height(0), m_pixels()
    {
        // Ouverture du fichier en mode binaire
        std::ifstream file(name, std::ios::in | std::ios::binary);

        // Vérification si le fichier est ouvert avec succès
        if (!file)
        {
            std::cerr << "Cannot open PPM file " << name << std::endl;
            exit(EXIT_FAILURE);
        }

        std::string MagicNumber, line;

        // Lecture du MagicNumber
        getLine(file, line);
        std::istringstream iss1(line);
        iss1 >> MagicNumber;

        // Vérification du MagicNumber (doit être "P6" pour un fichier binaire PPM)
        if (MagicNumber != "P6")
        {
            std::cerr << "Error reading PPM file " << name << ": unknown Magic Number \"" << MagicNumber
                      << "\". Only P6 is supported" << std::endl
                      << std::endl;
            exit(EXIT_FAILURE);
        }

        // Lecture de la taille de l'image
        getLine(file, line);
        std::istringstream iss2(line);

        int width, height;
        iss2 >> width >> height;

        // Vérification de la taille de l'image
        if (width <= 0 || height <= 0)
        {
            std::cerr << "Wrong image size " << width << " x " << height << std::endl;
            exit(EXIT_FAILURE);
        }

        // Mise à jour de la largeur et de la hauteur de la carte de hauteur
        m_width = width;
        m_height = height;

        // Lecture de la valeur maximale du canal
        int maxChannelVal;
        getLine(file, line);
        std::istringstream iss3(line);
        iss3 >> maxChannelVal;

        // Vérification de la valeur maximale du canal (doit être <= 255)
        if (maxChannelVal > 255)
        {
            std::cerr << "Max channel value too high in " << name << std::endl;
            exit(EXIT_FAILURE);
        }

        // Lecture des pixels
        std::vector<uint8_t> buffer = std::vector<uint8_t>(m_width * m_height * 3);
        for (uint32_t y = m_height; y-- > 0;)
        {
            // Lecture de chaque ligne
            file.read(reinterpret_cast<char *>(buffer.data() + (y * m_width) * 3), m_width * 3);
        }

        const std::size_t pixelNb = m_width * m_height;
        m_pixels = std::vector<uint8_t>(pixelNb);

        // Copie uniquement le canal rouge
        for (std::size_t i = 0; i < pixelNb; i++)
            m_pixels[i] = buffer[i * 3];
    }

    // Méthode privée pour lire une ligne du fichier en ignorant les commentaires
    void Heightmap::getLine(std::ifstream &file, std::string &s) const
    {
        for (;;)
        {
            // Lecture de la ligne du fichier
            if (!std::getline(file, s))
            {
                std::cerr << "Error reading PPM file" << std::endl;
                exit(EXIT_FAILURE);
            }

            // Recherche du premier caractère non vide et non commentaire
            std::string::size_type index = s.find_first_not_of("\n\r\t ");
            if (index != std::string::npos && s[index] != '#')
                break; // Sortie de la boucle si la ligne n'est pas un commentaire
        }
    }

    // Méthode pour sauvegarder la carte de hauteur dans un fichier PPM
    void Heightmap::saveTo(const char *name) const
    {
        // Ouverture du fichier en mode binaire en écriture
        std::ofstream file(name, std::ios::out | std::ios::trunc | std::ios::binary);

        // Écriture de l'en-tête PPM
        file << "P6" << std::endl;                       // Magic Number
        file << m_width << " " << m_height << std::endl; // Taille de l'image
        file << "255" << std::endl;                      // Valeur maximale pour les canaux R, G, B

        const std::size_t pixelNb = m_width * m_height;
        std::vector<uint8_t> buffer = std::vector<uint8_t>(pixelNb * 3);

        // Remplissage du tampon avec les valeurs de hauteur pour les canaux R, G, B
        for (std::size_t i = 0; i < pixelNb; i++)
        {
            const uint8_t height = m_pixels[i];
            buffer[i * 3 + 0] = height;
            buffer[i * 3 + 1] = height;
            buffer[i * 3 + 2] = height;
        }

        const uint8_t *const ptr = buffer.data();
        for (int y = m_height; y-- > 0;)
        {
            // Écriture de chaque ligne
            file.write((char *)(ptr + y * m_width * 3), m_width * 3);
        }

        // Fermeture du fichier
        file.close();
    }
} // namespace los
