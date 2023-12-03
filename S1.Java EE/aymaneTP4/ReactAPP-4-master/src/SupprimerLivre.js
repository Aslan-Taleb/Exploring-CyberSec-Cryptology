import React, { useState } from 'react';

const SupprimerLivreForm = ({ onSupprimerLivre }) => {
  // État pour stocker le titre du livre à supprimer
  const [titre, setTitre] = useState('');

  // Fonction pour gérer la soumission du formulaire
  const handleSupprimerLivre = (e) => {
    e.preventDefault();

    // Vérifier que le titre est renseigné
    if (!titre) {
      console.error('Veuillez remplir le champ Titre.');
      return;
    }

    // Appeler la fonction de suppression passée en tant que prop
    onSupprimerLivre(titre);
    
    // Réinitialiser le champ du formulaire après la soumission
    setTitre('');
  };

  return (
    <div>
      <h2>Supprimer un Livre</h2>
      <form onSubmit={handleSupprimerLivre}>
        <div>
          <label>Titre:</label>
          <input type="text" value={titre} onChange={(e) => setTitre(e.target.value)} />
        </div>
        <button type="submit">Supprimer Livre</button>
      </form>
    </div>
  );
};

export default SupprimerLivreForm;
