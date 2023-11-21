class AppComposant extends React.Component {
  constructor(props) {
    super(props);
    // Initialisation de l'état avec un tableau de facts vide, le total des facts et le compteur
    this.state = { facts: [], totalFacts: 0, compteurFacts: 0 };
  }

  // Fonction pour récupérer de nouvelles données depuis l'API
  fetchData() {
    // Limite du nombre de nouvelles données à récupérer
    const limit = 1;
    // Décalage pour spécifier où commencer à récupérer les données
    const offset = this.state.totalFacts;

    // Appel à l'API pour récupérer les données
    fetch(`https://jsonplaceholder.typicode.com/posts?_limit=${limit}&_start=${offset}`)
      .then(res => res.json())
      .then(data => {
        // Concaténer les nouvelles données avec les anciennes dans l'état
        this.setState(prevState => ({
          facts: [...prevState.facts, ...data],
          totalFacts: prevState.totalFacts + limit,
        }));
      });
  }

  // Fonction pour incrémenter le compteur et récupérer de nouvelles données
  compteurIncrementAndCompteur() {
    // Incrémentation du compteur
    this.setState({ compteurFacts: this.state.compteurFacts + 1 });
    // Appel à la fonction fetchData pour récupérer de nouvelles données
    this.fetchData();
  }

  render() {
    return (
      <div>
        {/* Affichage d'un lien et d'un bouton pour déclencher l'incrémentation et la récupération de données */}
        Random JSON from{' '}
        <a href="https://jsonplaceholder.typicode.com/">https://jsonplaceholder.typicode.com/</a>:
        <button onClick={() => this.compteurIncrementAndCompteur()}>Click Me</button>
        {/* Affichage du nombre de fois que le bouton a été cliqué */}
        <p>Nombre De Facts : {this.state.compteurFacts}</p>
        {/* Affichage des données récupérées sous forme de liste */}
        <ul>
          {this.state.facts.map(f => (
            <li key={f.id}>{f.title}</li>
          ))}
        </ul>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<AppComposant />);
