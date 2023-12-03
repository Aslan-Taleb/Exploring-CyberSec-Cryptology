import React, { useState } from 'react';

const AjouterLivre = () => {
  const [titre, setTitre] = useState('');
  const [auteur, setAuteur] = useState('');
  const [nbExemplaires, setNbExemplaires] = useState('');

  const handleAjouterLivre = async () => {
    try {
        // Vérifiez que les champs obligatoires sont remplis
        if (!titre || !auteur || !nbExemplaires) {
            console.error('Veuillez remplir tous les champs.');
            return;
        }

        // Utilisez URLSearchParams pour construire le corps de la requête
        const params = new URLSearchParams();
        params.append('titre', titre);
        params.append('auteur', auteur);
        params.append('nbExemplaires', nbExemplaires);

        // Effectuez la requête POST pour ajouter un livre
        const response = await fetch('http://localhost:8080/bibliotheque/addLivre', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: params,
        });

        // Vérifiez si la requête a réussi
        if (response.ok) {
            // Réinitialisez les champs du formulaire après avoir ajouté le livre
            setTitre('');
            setAuteur('');
            setNbExemplaires('');
            console.log('Livre ajouté avec succès!');
        } else {
            // Si la requête a échoué, traitez les erreurs
            console.error('Erreur lors de l\'ajout du livre:', response.status, response.statusText);
        }
    } catch (error) {
        // Gérez les erreurs liées à la requête
        console.error('Erreur lors de l\'ajout du livre:', error);
    }
};


  return (
    <div>
      <h1>Ajouter un Livre</h1>
      <form>
        <label>Titre:</label>
        <input type="text" value={titre} onChange={(e) => setTitre(e.target.value)} />

        <label>Auteur:</label>
        <input type="text" value={auteur} onChange={(e) => setAuteur(e.target.value)} />

        <label>Nombre d'exemplaires:</label>
        <input type="number" value={nbExemplaires} onChange={(e) => setNbExemplaires(e.target.value)} />

        <button type="button" onClick={handleAjouterLivre}>Ajouter Livre</button>
      </form>
    </div>
  );
};

export default AjouterLivre;
