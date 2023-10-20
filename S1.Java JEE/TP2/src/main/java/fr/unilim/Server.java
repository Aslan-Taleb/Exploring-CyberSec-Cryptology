package fr.unilim;

import jakarta.inject.Inject;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Path("/api")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class Server {
    @Inject
    HttpServletRequest request;

    private final Map<String, String> annuaire = new HashMap<>();

    private static final String ERROR_NOT_FOUND = "Tu dois être connecté";
    private static final String ERROR_BAD_REQUEST = "Les propriétés 'login' et 'password' doivent être renseignées";

    public Server() {
        annuaire.put("admin", "admin");
    }

    @GET
    @Path("/users")
    public List<String> listUsers() {
        if (isAuthenticated()) {
            return new ArrayList<>(annuaire.keySet());
        }
        return null;
    }

    @POST
    @Path("/add")
    public Response addUser(User user) {
        if (isAuthenticated()) {
            if (user.getLogin() != null && !user.getLogin().isEmpty() && user.getPassword() != null && !user.getPassword().isEmpty()) {
                annuaire.put(user.getLogin(), user.getPassword());
                return createResponse(Response.Status.OK, "Utilisateur ajouté");
            } else {
                return createResponse(Response.Status.BAD_REQUEST, ERROR_BAD_REQUEST);
            }
        }
        return createResponse(Response.Status.NOT_FOUND, ERROR_NOT_FOUND);
    }

    @DELETE
    @Path("/delete")
    public Response deleteUser(@QueryParam("login") String login) {
        if (isAuthenticated()) {
            if (annuaire.containsKey(login)) {
                annuaire.remove(login);
                return createResponse(Response.Status.OK, "Utilisateur supprimé");
            } else {
                return createResponse(Response.Status.NOT_FOUND, "Utilisateur non trouvé");
            }
        }
        return createResponse(Response.Status.NOT_FOUND, ERROR_NOT_FOUND);
    }

    @POST
    @Path("/authenticate")
    public Response authenticate(User user) {
        if (annuaire.containsKey(user.getLogin()) && annuaire.get(user.getLogin()).equals(user.getPassword())) {
            HttpSession session = request.getSession(true);
            session.setAttribute("user", user);
            return createResponse(Response.Status.OK, "Authentification réussie");
        } else {
            return createResponse(Response.Status.UNAUTHORIZED, "Authentification échouée");
        }
    }

    public boolean isAuthenticated() {
        HttpSession session = request.getSession(false);
        return session != null && session.getAttribute("user") != null;
    }

    @POST
    @Path("/logout")
    public Response logout() {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
            return createResponse(Response.Status.UNAUTHORIZED, "Session Invalide");
        } else {
            return createResponse(Response.Status.UNAUTHORIZED, "Déconnexion Réussie");
        }
    }

    private Response createResponse(Response.Status status, String entity) {
        return Response.status(status).entity(entity).build();
    }
}
