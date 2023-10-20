package fr.unilim;


import jakarta.enterprise.context.RequestScoped;

@RequestScoped
public class User {

    private String login;


    private String password;

    // Constructeur par défaut
    public User() {}

    // Getter et Setter pour le login
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    // Getter et Setter pour le mot de passe
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}


