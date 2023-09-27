package fr.unilim.exercice3;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(name = "ServletHate5", urlPatterns = {"/ServletHate5"})
public class ServletHate5 extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        response.setContentType("text/html");
        response.getWriter().println("<h1>Here We dont like 5</h1>");
        response.getWriter().println("<a href=\"/home\">Get Back</a>");
        for(int i = 1; i < 20; i++){
            if (i % 5 != 0){}
            response.getWriter().println("<p>" + i + "</p>");
        }
    }
}
