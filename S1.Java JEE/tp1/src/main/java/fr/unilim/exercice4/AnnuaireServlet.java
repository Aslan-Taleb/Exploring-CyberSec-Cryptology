package fr.unilim.exercice4;

import jakarta.servlet.ServletConfig;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebInitParam;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.FileStore;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

@WebServlet(
        name = "annuaire",
        urlPatterns = {"/annuaire"}
)
public class AnnuaireServlet extends HttpServlet {
    // Récupérez la HashMap des comptes à partir de la ServletContext
    private HashMap<String, String> accounts;

    @Override
    public void init(ServletConfig config) throws ServletException {
        super.init(config);

        // Access the ServletContext and retrieve the "accounts" attribute
        ServletContext servletContext = getServletContext();
        accounts = (HashMap<String, String>) servletContext.getAttribute("accounts");
    }
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws  IOException {
        // Handle account deletion
        boolean getDeleted = false;
        String nameToDelete = request.getParameter("suppr");
        if (nameToDelete != null && accounts.containsKey(nameToDelete)) {
            accounts.remove(nameToDelete);
            getDeleted = true;
        }
        // Generate HTML for the user input form
        String formHtml = "<form method=\"post\" action=\"/annuaire\">" +
                "Name: <label><input type=\"text\" name=\"username\"></label><br>" +
                "Password: <label><input type=\"password\" name=\"password\"></label><br>" +
                "<input type=\"submit\" value=\"Submit\">";

        // Generate HTML for the account list
        StringBuilder accountHtml = new StringBuilder();
        accountHtml.append("<h2>List of Accounts:</h2>");

        accountHtml.append("<ul>");
        for (Map.Entry<String, String> entry : accounts.entrySet()) {
            String key = entry.getKey();
            accountHtml.append("<li>").append(key).append("</li>");
        }
        accountHtml.append("</ul>");

        // Set the content type of the response to HTML
        response.setContentType("text/html");

        // Write the HTML content to the response
        PrintWriter out = response.getWriter();
        out.println("<html><head><title>Annuaire</title></head><body><h1>Annuaire</h1>");
        out.println(formHtml);
        if (getDeleted) {
            out.println(" <p>Account with name <strong>" + nameToDelete + "</strong> has been deleted.</p>");
        }
        out.println(accountHtml);
        out.println("<a href=\"/login\">logout</a>");
        out.println("<a href=\"/\">Get Back</a>");
        out.println("</body></html>");

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException{
        // Retrieve user input
        String name = request.getParameter("username");
        String password = request.getParameter("password");
        // Add the account to the HashMap
        accounts.put(name, password);
        doGet(request, response);
    }
}
