package fr.unilim.exercice1;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet(name = "servletSayHello2", urlPatterns = {"/servletSayHello2"})
public class ServletSayHello2 extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");
        response.getWriter().println("<h1>Hello World ! </h1>");
        response.getWriter().println("<a href=\"/\">Get Back</a>");
    }
}
