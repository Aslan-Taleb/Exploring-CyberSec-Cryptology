import React from 'react';

const ObtenirListeButton = () => {
  const handleButtonClick = async () => {
    console.log('Button clicked'); 
    try {
      // Make an HTTP GET request to http://localhost:8080/bibliotheque/obtenirListe
      const response = await fetch('http://localhost:8080/bibliotheque/obtenirListe');

      // Check if the request was successful
      if (response.ok) {
        // Do something with the response data (e.g., log it)
        const responseData = await response.json();
        console.log(responseData);
      } else {
        // Handle errors
        console.error('HTTP request failed:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error during HTTP request:', error);
    }
  };

  return (
    <div>
      <h2>My Component</h2>
      <button onClick={handleButtonClick}>Get Book List</button>
    </div>
  );
};

export default ObtenirListeButton;
