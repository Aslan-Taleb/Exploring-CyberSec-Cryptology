package fr.unilim;

import jakarta.inject.Inject;
import jakarta.persistence.EntityManager;
import jakarta.persistence.NoResultException;
import jakarta.persistence.NonUniqueResultException;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import java.util.List;

@Path("/server")
public class Server {

    private final EntityManager entityManager;

    @Inject
    public Server(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    @POST
    @Path("/add")
    @Transactional
    public String ajouterLivre(
            @FormParam("titre") String titre,
            @FormParam("auteur") String auteur,
            @FormParam("nbExemplaires") int nbExemplaires) {
        Livre newLivre = new Livre(titre, auteur, nbExemplaires);
        entityManager.persist(newLivre);
        return "Success";
    }

    @GET
    @Path("/list")
    @Produces(MediaType.TEXT_HTML)
    public String obtenirListe() {
        List<Livre> listeLivres = entityManager
                .createQuery("SELECT l FROM Livre l", Livre.class)
                .getResultList();

        StringBuilder html = new StringBuilder();
        html.append("<html>");
        html.append("<head>");
        html.append("<title>Liste des Livres</title>");
        html.append("</head>");
        html.append("<body>");
        html.append("<h1>Liste des Livres</h1>");
        html.append("<ul>");

        if (!listeLivres.isEmpty()) {
            for (Livre livre : listeLivres) {
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

        try {
            Livre livreTrouve = entityManager
                    .createQuery("SELECT l FROM Livre l WHERE l.titre = :titre", Livre.class)
                    .setParameter("titre", titre)
                    .getSingleResult();

            html.append("<h2>").append(livreTrouve.getTitre()).append("</h2>");
            html.append("<p>Auteur : ").append(livreTrouve.getAuteur()).append("</p>");
            html.append("<p>Nombre d'exemplaires : ").append(livreTrouve.getNombreExemplaires()).append("</p>");
        } catch (NoResultException e) {
            html.append("Aucun livre trouvé pour le titre : ").append(titre);
        } catch (NonUniqueResultException e) {
            html.append("Plusieurs livres trouvés pour le titre : ").append(titre);
        } catch (Exception e) {
            html.append("Erreur lors de la recherche.");
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
        try {
            Livre livreToUpdate = entityManager
                    .createQuery("SELECT l FROM Livre l WHERE l.titre = :titre", Livre.class)
                    .setParameter("titre", titre)
                    .getSingleResult();

            if (livreToUpdate.getTitre().equalsIgnoreCase(titre)) {
                livreToUpdate.setNombreExemplaires(nbExemplaires);
                return "Success";
            }
        } catch (NoResultException e) {
            return "Livre non trouvé pour le titre : " + titre;
        } catch (NonUniqueResultException e) {
            return "Plusieurs livres trouvés pour le titre : " + titre;
        } catch (Exception e) {
            return "Erreur lors de la mise à jour.";
        }

        return "error";
    }

    @POST
    @Path("/delete")
    public String supprimerLivre(@FormParam("titre") String titre) {
        try {
            Livre livreASupprimer = entityManager
                    .createQuery("SELECT l FROM Livre l WHERE l.titre = :titre", Livre.class)
                    .setParameter("titre", titre)
                    .getSingleResult();

            if (livreASupprimer != null) {
                entityManager.remove(livreASupprimer);
                return "Success";
            } else {
                return "Livre non trouvé pour le titre : " + titre;
            }
        } catch (NoResultException e) {
            return "Livre non trouvé pour le titre : " + titre;
        } catch (NonUniqueResultException e) {
            return "Plusieurs livres trouvés pour le titre : " + titre;
        } catch (Exception e) {
            return "Erreur lors de la suppression.";
        }
    }
}

