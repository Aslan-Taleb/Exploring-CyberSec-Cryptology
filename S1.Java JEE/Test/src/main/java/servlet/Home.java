package servlet;

import java.io.*;

import beans.Prof;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;


@WebServlet("/Home")
public class Home extends HttpServlet {
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
        String name = request.getParameter("name");
        if (name == null){
            name = "World";
        }
        request.setAttribute("welcomeMessage","Hello " + name +" ! ");
        String [] modules = {"IA","Programmation Reseaux","Java EE"};
        request.setAttribute("modules",modules);
        Prof EC = new Prof();
        EC.setNom("Conchon");
        EC.setPrenom("Emmanuel");
        EC.setEmail("EmmanuelConchon@gmail.com");
        EC.setActif(true);
        request.setAttribute("profJEE",EC);

        this.getServletContext().getRequestDispatcher("/WEB-INF/home.jsp").forward(request, response);

    }

    public void destroy() {
    }
}