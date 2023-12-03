package fr.unilim.exercice2;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "ServletCountWithUser", urlPatterns = {"/ServletCountWithUser"})
public class ServletCountWithUser extends HttpServlet {

    // Cette méthode est appelée lorsqu'une requête GET est effectuée sur l'URL spécifié dans @WebServlet
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // Définir le type de contenu de la réponse comme HTML
        response.setContentType("text/html");
        
        // Obtenir la session associée à la requête
        HttpSession session = request.getSession();

        // Identifier l'utilisateur (ici, l'ID est défini comme "AslaN")
        String userID = "AslaN";

        // Obtenir le compteur spécifique à l'utilisateur à partir de la session
        Integer count = (Integer) session.getAttribute(userID);

        // Si l'utilisateur n'a jamais été compté, initialiser le compteur à 1 ; sinon, l'incrémenter
        if (count == null) {
            count = 1;
        } else {
            count++;
        }

        // Mettre à jour le compteur spécifique à l'utilisateur dans la session
        session.setAttribute(userID, count);

        // Préparer le flux de sortie pour écrire la réponse HTML
        PrintWriter out = response.getWriter();

        // Générer la structure de base du document HTML
        out.println("<html>");
        out.println("<body>");

        // Afficher le titre de la page avec le compteur spécifique à l'utilisateur
        out.println("<h1>Here We Count With Users</h1>");
        out.println("<p>L'utilisateur <strong>" + userID + "</strong> nous a contactés <strong>" + count + " fois</strong>.</p>");

        // Ajouter un lien pour revenir à la page d'accueil
        out.println("<a href=\"/\">Get Back</a>");

        // Fermer la structure du document HTML
        out.println("</body>");
        out.println("</html>");

        // Fermer le flux de sortie
        out.close();
    }
}
