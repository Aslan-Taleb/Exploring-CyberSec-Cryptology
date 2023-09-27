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
        import java.util.HashMap;

        @WebServlet(
                name = "login",
                urlPatterns = {"/login"},
                initParams = {
                @WebInitParam(name = "usernameParam", value = "AslaN"),
                @WebInitParam(name = "passwordParam", value = "1234"),

        }
        )
        public class Login extends HttpServlet {
            private final HashMap<String, String> accounts = new HashMap<>();

            @Override
            public void init(ServletConfig config) throws ServletException {
                super.init(config);
                // Access initialization parameters "usernameParam" and "passwordParam"
                String username = getServletConfig().getInitParameter("usernameParam");
                String password = getServletConfig().getInitParameter("passwordParam");
                // Initialize your "accounts" data structure with these values
                accounts.put(username, password);
                System.out.println("Initialization complete");
                this.getServletContext().setAttribute("accounts", accounts);
            }

            @Override
            protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
                // Vérifiez si l'utilisateur est déjà authentifié
                HttpSession session = request.getSession(false);
                if (session != null && session.getAttribute("authenticatedUser") != null) {
                    // Redirigez l'utilisateur vers la page de l'annuaire s'il est déjà authentifié
                    response.sendRedirect(request.getContextPath() + "/annuaire");
                } else {
                    // Affichez la page de connexion
                    response.sendRedirect(request.getContextPath() + "/login.html");
                }
            }

            @Override
            protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
                // Récupérez les informations du formulaire de connexion
                String username = request.getParameter("username");
                String password = request.getParameter("password");

                // Vérifiez l'authentification en utilisant la HashMap des comptes
                boolean isAuthenticated = checkAuthentication(username, password);

                if (isAuthenticated) {
                    // Si l'authentification réussit, créez une session et stockez des informations d'authentification
                    HttpSession session = request.getSession(true);
                    session.setAttribute("authenticatedUser", username);

                    // Redirigez l'utilisateur vers la page de l'annuaire
                    response.sendRedirect(request.getContextPath() + "/annuaire");
                } else {
                    // Si l'authentification échoue, affichez un message d'erreur et redirigez vers la page de connexion
                    PrintWriter out = response.getWriter();
                    out.println("<html><head><title>Login Error</title></head><body>");
                    out.println("<p>Login failed. Please try again.</p>");
                    out.println("<a href=\"/login.html\">Back to Login</a>");
                    out.println("</body></html>");
                }
            }

            // Méthode pour vérifier l'authentification en utilisant la HashMap des comptes
            private boolean checkAuthentication(String username, String password) {

                System.out.println(accounts);
                if (accounts.containsKey(username)) {
                    // Vérifiez si le nom d'utilisateur correspond au mot de passe
                    String storedPassword = accounts.get(username);
                    return storedPassword != null && storedPassword.equals(password);
                }

                return false; // Authentification échouée
            }
        }

