package fr.unilim;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Livre {

    @Id
    @GeneratedValue
    private Long id;
    @Column
    private String titre;
    @Column
    private String auteur;
    @Column
    private int nombreExemplaires;

    // Constructeur par défaut
    public Livre(String titre,String auteur,int nbExemplaires) {
        this.titre = titre;
        this.auteur = auteur;
        this.nombreExemplaires = nbExemplaires;

    }

    public Livre() {

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