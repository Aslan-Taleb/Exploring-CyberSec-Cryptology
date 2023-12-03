import React, { useState } from 'react';

const MettreAJourForm = ({ onMettreAJour }) => {
  // États pour stocker le titre et le nombre d'exemplaires à mettre à jour
  const [titre, setTitre] = useState('');
  const [nbExemplaires, setNbExemplaires] = useState('');

  // Fonction pour gérer la soumission du formulaire
  const handleMettreAJour = (e) => {
    e.preventDefault();

    // Vérifier que le titre et le nombre d'exemplaires sont renseignés
    if (!titre || !nbExemplaires) {
      console.error('Veuillez remplir tous les champs.');
      return;
    }

    // Appeler la fonction de mise à jour passée en tant que prop
    onMettreAJour(titre, parseInt(nbExemplaires));
    
    // Réinitialiser les champs du formulaire après la soumission
    setTitre('');
    setNbExemplaires('');
  };

  return (
    <div>
      <h2>Mettre à Jour le Nombre d'Exemplaires</h2>
      <form onSubmit={handleMettreAJour}>
        <div>
          <label>Titre:</label>
          <input type="text" value={titre} onChange={(e) => setTitre(e.target.value)} />
        </div>
        <div>
          <label>Nouveau Nombre d'Exemplaires:</label>
          <input type="number" value={nbExemplaires} onChange={(e) => setNbExemplaires(e.target.value)} />
        </div>
        <button type="submit">Mettre à Jour</button>
      </form>
    </div>
  );
};

export default MettreAJourForm;
