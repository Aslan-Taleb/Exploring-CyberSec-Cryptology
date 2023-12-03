import React, { useState } from 'react';

const ObtenirListeButton = () => {
  const [livres, setLivres] = useState([]);

  const obtenirListe = async () => {
    try {
        const response = await fetch('http://localhost:8080/bibliotheque/obtenirListe');
        if (response.ok) {
            const data = await response.json();
           

            // Assurez-vous que la réponse est un tableau avant d'appeler map
            if (Array.isArray(data)) {
                setLivres(data);
            } else {
                console.error('La réponse n\'est pas un tableau:', data);
            }
        } else {
            console.error('Erreur lors de la récupération de la liste des livres:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Erreur lors de la récupération de la liste des livres:', error);
    }
};

return (
    <div>
        {/* ... */}
        <button onClick={obtenirListe}>Obtenir la liste des livres</button>

        <ul>
            {/* Vérifiez que livres est un tableau avant d'appeler map */}
            {Array.isArray(livres) ? (
                livres.map((livre, index) => (
                    <li key={index}>{livre.titre} - {livre.auteur} - {livre.nbExemplaires} exemplaires</li>
                ))
            ) : (
                <li>La liste des livres n'est pas disponible.</li>
            )}
        </ul>
    </div>
);
};

export default ObtenirListeButton;
