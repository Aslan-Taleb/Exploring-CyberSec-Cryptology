package fr.unilim;

import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import java.util.ArrayList;
import java.util.List;

@Path("/server")
public class Server {
    private final List<Livre> livres = new ArrayList<>();


    @POST
    @Path("/add")
    public String ajouterLivre(
            @FormParam("titre") String titre,
            @FormParam("auteur") String auteur,
            @FormParam("nbExemplaires") int nbExemplaires) {
        if (titre != null && !titre.isEmpty() && nbExemplaires >= 0) {
            Livre newLivre = new Livre(titre, auteur, nbExemplaires);
            livres.add(newLivre);
            return "Success" ;
        } else {
            return "error";
        }
    }

    @GET
    @Path("/list")
    @Produces(MediaType.TEXT_HTML)
    public String obtenirListe() {
        StringBuilder html = new StringBuilder();
        html.append("<html>");
        html.append("<head>");
        html.append("<title>Liste des Livres</title>");
        html.append("</head>");
        html.append("<body>");
        html.append("<h1>Liste des Livres</h1>");
        html.append("<ul>");

        if (livres != null && !livres.isEmpty()) {
            for (Livre livre : livres) {
                html.append("<li>");
                html.append("<h2>").append(livre.getTitre()).append("</h2>");
                html.append("<p>Auteur : ").append(livre.getAuteur()).append("</p>");
                html.append("<p>Nombre d'exemplaires : ").append(livre.getNombreExemplaires()).append("</p>");
                html.append("</li>");
            }
            html.append("</ul>");
        } else {
            html.append("<li>Aucun Livre Pour L'instant !</li>");
        }

        html.append("<a href='../index.html'>Retour à la page d'accueil</a>");
        html.append("</body>");
        html.append("</html>");
        return html.toString();
    }

    @GET
    @Path("/search")
    @Produces(MediaType.TEXT_HTML)
    public String rechercherParTitre(@QueryParam("titre") String titre) {
        StringBuilder html = new StringBuilder();
        html.append("<html>");
        html.append("<head>");
        html.append("<title>Résultat de la recherche</title>");
        html.append("</head>");
        html.append("<body>");

        boolean livreTrouve = false;

        for (Livre livre : livres) {
            if (livre.getTitre().equalsIgnoreCase(titre)) {
                html.append("<h2>").append(livre.getTitre()).append("</h2>");
                html.append("<p>Auteur : ").append(livre.getAuteur()).append("</p>");
                html.append("<p>Nombre d'exemplaires : ").append(livre.getNombreExemplaires()).append("</p>");
                livreTrouve = true;
                break; // Pas besoin de continuer la recherche
            }
        }

        if (!livreTrouve) {
            html.append("Aucun livre trouvé pour le titre : ").append(titre);
        }

        html.append("<a href='../index.html'>Retour à la page d'accueil</a>");
        html.append("</body>");
        html.append("</html>");

        return html.toString();
    }

    @POST
    @Path("/update")
    public String mettreAJourNbExemplaire(
            @FormParam("titre") String titre,
            @FormParam("nbExemplaires") int nbExemplaires) {
        for (Livre livre : livres) {
            if (livre.getTitre().equalsIgnoreCase(titre)) {
                livre.setNombreExemplaires(nbExemplaires);
                return "Success";
            }
        }

        return "error";
    }

    @POST
    @Path("/delete")
    public String supprimerLivre(@FormParam("titre") String titre) {
        Livre livreASupprimer = null;
        for (Livre livre : livres) {
            if (livre.getTitre().equalsIgnoreCase(titre)) {
                livreASupprimer = livre;
                break;
            }
        }

        if (livreASupprimer != null) {
            livres.remove(livreASupprimer);
            return "Success";
        }

        return "error";
    }
}
