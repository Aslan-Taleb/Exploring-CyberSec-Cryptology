<%--
  Created by IntelliJ IDEA.
  User: AslaN
  Date: 14/09/2023
  Time: 15:20
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Mon Profil</title>
    <style>
        /* Appliquer un style au corps de la page */
        body {
            display: flex;
            flex-direction: column; /* Aligner les éléments verticalement */
            align-items: center; /* Centrer les éléments horizontalement */
            justify-content: flex-start; /* Aligner les éléments en haut */
            height: 100vh;
            margin: 0; /* Supprimer la marge par défaut du corps */
        }

        /* Appliquer un style au menu (header) */
        header {
            background-color: #333;
            color: white;
            padding: 10px;
            width: 100%;
            text-align: center;
        }

        p {
            text-align: center; /* Centrer le texte dans le paragraphe */
            margin-top: 20px; /* Ajouter un espace entre le menu et le texte */
        }
    </style>
</head>
<body>
<header>
    <%@ include file="menu.jsp" %>
</header>
<p>
    🦁 Étudiant en Master Sécurité Informatique.<br>
    💾 GitHub : <a href="https://github.com/Aslan-Taleb">github.com/Aslan-Taleb</a><br>
    📧 Adresse e-mail : <a href="mailto:aslantalebselim@gmail.com">aslantalebselim@gmail.com</a>
</p>
</body>
</html>
