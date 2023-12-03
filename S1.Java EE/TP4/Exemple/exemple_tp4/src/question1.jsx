import React from 'react';
import axios from 'axios';

class ApiAsker extends React.Component {
  constructor(props) {
    super(props);
    this.state = { facts: [], compteur: 0 };
  }
  //componentDidMount est une méthode du cycle de vie des composants React. Elle est appelée automatiquement par React après qu'un composant a été ajouté au DOM
  componentDidMount() {
    // Appeler la requête API une fois que le composant est monté
    this.requeteAPI();
  }

  requeteAPI() {
    axios.get('https://jsonplaceholder.typicode.com/posts?_limit=10')
      .then(res => {
        this.setState({ facts: res.data });
      })
      .catch(error => {
        console.error("Une erreur s'est produite lors de la récupération des articles :", error);
      });
  }

  afficherArticle() {
    return (
      <ul>
        {this.state.facts.slice(0, this.state.compteur).map(f => <li key={f.id}>{f.title}</li>)}
      </ul>
    );
  }

  compteurIncrement() {
    // Modifiez l'état dans une fonction qui est appelée par un événement, pas directement dans render
    this.setState({ compteur: this.state.compteur + 1 });
  }

  render() {
    return (
      <div>
        Random JSON from <a href="https://jsonplaceholder.typicode.com/">https://jsonplaceholder.typicode.com/</a>:
        <button onClick={() => this.compteurIncrement()}>Another One ! </button>
        {this.afficherArticle()}
      </div>
    );
  }
}

export default ApiAsker;
