
import React from 'react';

//creation d'une classe pour regrouper les methodes et les variables
class ExempleButton extends React.Component {
  //le constructeur avec comme variable compteur mit a 0
  constructor(props) {
    super(props)
    this.state =  { compteur : 0 }
  }
  //une methode qui modifie les variables donc on utlise setStat
  //apres on dit que compteur = compteur+1 mais en js donc ca donne ca
  compteurIncrement() {
    this.setState( { compteur: this.state.compteur + 1 })
  }
  //une fonction render qui ne fais que afficher
  //la on a utiliser bouton donc quand on clique on appel la methode
  //compteurIncrement(pour augmenter le compteur)
  //puis on a appeler Compteur qu'on a definis plus car oui c'est comme ca qu'oin appel
  //une methode on lui donnant comme parametre bah le compteur
  render() {
    return(
      <div>
        <button onClick={ () => this.compteurIncrement()}>Click Me</button>
        <Compteur valeur= { this.state.compteur }/>
      </div>
    )
  }
}


function Compteur({ valeur }) {
  return(
    <div>Valeur du compteur : {valeur}</div>
  )
}

export default ExempleButton