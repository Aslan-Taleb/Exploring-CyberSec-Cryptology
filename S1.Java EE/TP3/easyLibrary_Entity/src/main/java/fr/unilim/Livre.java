package fr.unilim;

public class Livre {
    private String titre;
    private String auteur;
    private int nombreExemplaires;

    // Constructeur par défaut
    public Livre(String titre,String auteur,int nbExemplaires) {
        this.titre = titre;
        this.auteur = auteur;
        this.nombreExemplaires = nbExemplaires;

    }

    // Getters et Setters pour le titre
    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }

    // Getters et Setters pour l'auteur
    public String getAuteur() {
        return auteur;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }

    // Getters et Setters pour le nombre d'exemplaires
    public int getNombreExemplaires() {
        return nombreExemplaires;
    }

    public void setNombreExemplaires(int nombreExemplaires) {
        this.nombreExemplaires = nombreExemplaires;
    }
}

