package com.example.dossier;

import java.io.*;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

@WebServlet()
public class leTest extends HttpServlet {
    private String message;

    public void init() {
        message = "Hi ! \nThis is my first servlet!\n";
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        /*
        version des tipeu
        response.setContentType("text/html");
        response.setCharacterEncoding("UTF-8");

        // Hello
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h1>" + message + "</h1>");
        out.println("</body></html>");
        */
        this.getServletContext().getRequestDispatcher("/WEB-INF/home.jsp").forward(request, response);

    }

    public void destroy() {
    }
}