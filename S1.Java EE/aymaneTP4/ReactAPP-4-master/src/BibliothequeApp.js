import React, { useState } from 'react';
import AjouterLivreForm from './AjouterLivreForm';
import RechercherLivreForm from './RechercherLivreForm';
import ObtenirListeButton from './ObtenirListeButton';
import MettreAJourForm from './MettreAJourForm'; 
import SupprimerLivreForm from './SupprimerLivre';

const BibliothequeApp = () => {
  const [livres, setLivres] = useState([]);

  

  const ajouterLivre = (nouveauLivre) => {
    // Envoyez la requête pour ajouter le livre à votre API
    // Mettez à jour l'état des livres après l'ajout réussi
    setLivres([...livres, nouveauLivre]);
  };

  const rechercherLivre = async (titre) => {
  try {
    // Utilisez la fonction fetch pour effectuer une requête GET avec le paramètre de recherche
    const response = await fetch(`http://localhost:8080/bibliotheque/rechercherParTitre?titre=${encodeURIComponent(titre)}`);

    // Vérifiez si la requête a réussi
    if (response.ok) {
      // Récupérez les données de la réponse
      const result = await response.json();
        console.log("c good");
      // Mettez à jour l'état des livres avec les résultats de la recherche
      setLivres(result);
    } else {
      // Si la requête a échoué, traitez les erreurs
      console.error('Erreur lors de la recherche du livre:', response.status, response.statusText);
    }
  } catch (error) {
    // Gérez les erreurs liées à la requête
    console.error('Erreur lors de la recherche du livre:', error);
  }
};


const obtenirListe = async () => {
    try {
      // Utilisez la fonction fetch pour effectuer une requête GET
      const response = await fetch('http://localhost:8080/bibliotheque/obtenirListe');
  
      // Vérifiez si la requête a réussi
      if (response.ok) {
        // Récupérez les données de la réponse
        const result = await response.json();
        
        // Mettez à jour l'état des livres avec la liste obtenue
        setLivres(result);
      } else {
        // Si la requête a échoué, traitez les erreurs
        console.error('Erreur lors de l\'obtention de la liste des livres:', response.status, response.statusText);
      }
    } catch (error) {
      // Gérez les erreurs liées à la requête
      console.error('Erreur lors de l\'obtention de la liste des livres:', error);
    }
  };
  // Fonction pour mettre à jour le nombre d'exemplaires
  const mettreAJourNbreExemplaires = async (titre, nbExemplaires) => {
    try {
      const response = await fetch(`http://localhost:8080/bibliotheque/mettreAJourNbreExemplaires?titre=${encodeURIComponent(titre)}&nbExemplaires=${nbExemplaires}`, {
        method: 'POST',
      });

      if (response.ok) {
        // Si la requête a réussi, mettre à jour l'état des livres avec la liste mise à jour
        const result = await response.json();
        console.log('Mise à jour effectuée avec succès\n '+result);
      } else {
        // Si la requête a échoué, traiter les erreurs
        console.error('Erreur lors de la mise à jour du nombre d\'exemplaires:', response.status, response.statusText);
      }
    } catch (error) {
      // Gérer les erreurs liées à la requête
      console.error('Erreur lors de la mise à jour du nombre d\'exemplaires:', error);
    }
  };

  const handleSupprimerLivre = async (titre) => {
    try {
      const response = await fetch('http://localhost:8080/bibliotheque/supprimerLivre', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ titre: titre }),
      });

      if (response.ok) {
        // Mise à jour de la liste des livres après la suppression
        obtenirListe();
        console.log('Livre supprimé avec succès!');
      } else {
        console.error('Erreur lors de la suppression du livre:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Erreur lors de la suppression du livre:', error);
    }
  };
  

  return (
    <div>
      <h1>Application Bibliotheque</h1>
      <AjouterLivreForm onAjouterLivre={ajouterLivre} />
      <RechercherLivreForm onRechercherLivre={rechercherLivre} />
      <h2>Liste des Livres</h2>
      <ObtenirListeButton onObtenirListe={obtenirListe} />
      <MettreAJourForm onMettreAJour={mettreAJourNbreExemplaires} />
      <SupprimerLivreForm onSupprimerLivre={handleSupprimerLivre} />  {/* Utilisation du composant SupprimerLivreForm */}

      {/* Afficher la liste des livres */}
      
      <ul>
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

export default BibliothequeApp;
