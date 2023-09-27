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

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");
        HttpSession session = request.getSession();
        String ID = "AslaN";
        Integer count = (Integer) session.getAttribute(ID);
        if (count == null) {
            count = 1;
        }
        else{
            count++;
        }
        session.setAttribute(ID, count);
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<body>");
        out.println("<h1>Here We Count With Users</h1>");
        out.println("<p>L'utilisateur <strong>" + ID + "</strong> nous a contactés <strong>" + count + " fois</strong>.</p>");
        out.println("<a href=\"/home\">Get Back</a>");
        out.println("</body>");
        out.println("</html>");
        out.close();



    }
}
