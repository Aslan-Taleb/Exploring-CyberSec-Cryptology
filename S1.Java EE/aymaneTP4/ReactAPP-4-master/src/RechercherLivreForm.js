import React, { useState } from 'react';

const RechercherLivreForm = ({ onRechercherLivre, livres }) => {
  const [titre, setTitre] = useState('');

  const handleRechercherLivre = () => {
    onRechercherLivre(titre);
  };

  
  return (
    <div>
      <h2>Rechercher un Livre par Titre</h2>
      <div>
        <label>Titre:</label>
        <input type="text" value={titre} onChange={(e) => setTitre(e.target.value)} />
      </div>
      <button onClick={handleRechercherLivre}>Rechercher Livre</button>
    </div>
  );
};

export default RechercherLivreForm;
