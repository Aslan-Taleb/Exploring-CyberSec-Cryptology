<%--
  Created by IntelliJ IDEA.
  User: AslaN
  Date: 14/09/2023
  Time: 14:56
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Home Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }

        header {
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
        }

        h1 {
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
        }

        section {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #333;
            color: white;
        }

        h3 {
            color: #333;
        }
    </style>
</head>
<body>

<header>
    <%@ include file="menu.jsp" %>
</header>

<h1><%
    String varWelcome = (String) request.getAttribute("welcomeMessage");
    out.println(varWelcome);
%></h1>

<section>
    <h2>Apprentissage de Java EE</h2>
    <p>Je suis en train d'apprendre le Java EE..</p>

    <h3>Exemple d'utilisation de EL (Expression Language) :</h3>
    <table border="1">
        <tr>
            <th>${modules[0]}</th>
            <th>${modules[1]}</th>
            <th>${modules[2]}</th>
        </tr>
    </table>

    <h3>Exemple d'utilisation des Java Beans :</h3>
    <p><strong>Nom :</strong> ${profJEE.nom}</p>
    <p><strong>Prénom :</strong> ${profJEE.prenom}</p>
    <p><strong>Email :</strong> ${profJEE.email}</p>
    ${profJEE.actif ? 'Ce professeur est actif' : 'Ce professeur n\'est pas actif'}
</section>
</body>
</html>
