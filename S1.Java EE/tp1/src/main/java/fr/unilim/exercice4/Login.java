        package fr.unilim.exercice4;

        import jakarta.servlet.ServletConfig;
        import jakarta.servlet.ServletException;
        import jakarta.servlet.annotation.WebInitParam;
        import jakarta.servlet.annotation.WebServlet;
        import jakarta.servlet.http.HttpServlet;
        import jakarta.servlet.http.HttpServletRequest;
        import jakarta.servlet.http.HttpServletResponse;

        import java.io.IOException;
        import java.util.HashMap;

        @WebServlet(
                name = "login",
                urlPatterns = {"/login"},
                initParams = {
                @WebInitParam(name = "usernameParam", value = "admin"),
                @WebInitParam(name = "passwordParam", value = "admin"),

        }
        )
        public class Login extends HttpServlet {
            private final HashMap<String, String> accounts = new HashMap<>();
            private boolean isAuthenticated = false;
            //Utilisation de la fonction "init" qui sera executer une seule fois au debut
            //quand "/login" sera acceder pour la premiere fois
            @Override
            public void init(ServletConfig config) throws ServletException {
                super.init(config);
                
                String username = getServletConfig().getInitParameter("usernameParam");
                String password = getServletConfig().getInitParameter("passwordParam");
                // Initialize your "accounts" data structure with these values
                accounts.put(username, password);
                System.out.println("Initialization complete");
                this.getServletContext().setAttribute("accounts", accounts);
            }

            @Override
            protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
                // Vérifiez si l'utilisateur est déjà authentifié
                if (isAuthenticated) {
                    // Redirigez l'utilisateur vers la page de l'annuaire s'il est déjà authentifié
                    isAuthenticated = false;
                    response.sendRedirect(request.getContextPath() + "/annuaire");
                } else {
                    // Affichez la page de connexion
                    response.sendRedirect(request.getContextPath() + "/login.html");
                }
            }

            @Override
            protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
                // Récupérez les informations du formulaire de connexion
                String username = request.getParameter("username");
                String password = request.getParameter("password");

                // Vérifiez l'authentification en utilisant la HashMap des comptes
                isAuthenticated = checkAuthentication(username, password);

                if (!isAuthenticated) {
                    // Si l'authentification échoue, affichez un message d'erreur et redirigez vers la page de connexion
                    response.sendRedirect(request.getContextPath() + "/badLog.html");
                }
                doGet(request, response);
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

