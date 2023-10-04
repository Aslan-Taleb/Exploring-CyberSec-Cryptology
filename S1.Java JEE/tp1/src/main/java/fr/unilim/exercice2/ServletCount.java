package fr.unilim.exercice2;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

    @WebServlet(name = "ServletCount", urlPatterns = {"/ServletCount"})
public class ServletCount extends HttpServlet {
    private static Integer count = 0;

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");
        response.getWriter().println("<h1>Here We Count</h1>");
        count++;
        response.getWriter().println(count);
        response.getWriter().println("<a href=\"/\">Get Back</a>");
    }
}
