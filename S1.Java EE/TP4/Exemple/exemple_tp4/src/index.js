import React from 'react';
import ReactDOM from 'react-dom';
import IsayCestCool from './exemple1';
import ExempleButton from './exemple2';
import R from './exemple3';
import ApiAsker from './question1';







//Methode 1
// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(<ExempleComponent />);


ReactDOM.render(
<div> 
  <h1>Les Exemples TP 4 JEE</h1>
  <h2>Exemple 1 : (fonction qui dit c'est cool)</h2>
  <IsayCestCool />
  <h2>Exemple 2 : (Bouton + compteur)</h2>
  <ExempleButton />
  <h2>Exemple 3 : (Appel d'un api et affichage)</h2>
    <R />
  <h2>Question : (Appel d'un api et affichage)</h2>
  <ApiAsker />
</div>


,document.getElementById('root'));




