import logo from './Sans titre.jpeg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Dr. Tryhard <code>Dr. SuperToba</code> Moul CS
        </p>
        <a
          className="App-link"
          href="http://localhost:8080/bibliotheque/obtenirListe"
          target="_blank"
          rel="noopener noreferrer"
        >
          Obtenir Liste
        </a>
      </header>
    </div>
  );
}

export default App;

