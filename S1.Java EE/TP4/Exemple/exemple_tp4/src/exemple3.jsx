import axios from 'axios';
import React from 'react';



class R extends React.Component {
  constructor(props) {
    super(props)
    this.state = { facts: [] }
  }
  //methode qui fais un get sur un api
  //une fois la requete passer on un then (on dit c'est une promesse)
  //donc une fois la requete reussi on la resultat dans res ,
  //ce res on va prendre la data et le mettre dans facts
  componentDidMountOld() {
    axios.get(
        `https://jsonplaceholder.typicode.com/posts?_limit=5`)
            .then(res => { this.setState( 
                { facts: res.data } 
            );
        })
    
  }
  //autre methode pour le faire on utlise fetch
  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(res => res.json())
      .then(data => this.setState( { facts : data } ));
  }
  //difference : 
  //En général, si vous avez besoin d'une interface plus 
  //conviviale avec une gestion automatique des erreurs, des transformations de données 
  //et d'autres fonctionnalités avancées, axios est souvent préféré.
  //Si vous cherchez une solution intégrée et légère pour les projets plus simples 
  //ou si la taille de la bibliothèque est une préoccupation, fetch peut être une option appropriée.

  render() {
    return(
    <div>Random JSON from <a href="https://jsonplaceholder.typicode.com/">https://jsonplaceholder.typicode.com/</a>:
      <ul>
        
        { this.state.facts.map( f => <li key={f.id}>{ f.title} </li>) }
      </ul>
    </div>)
  }
  //le map la c'est une boucle en js et on recup que le id et le titre
}

export default R
