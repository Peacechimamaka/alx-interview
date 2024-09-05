#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make an HTTP GET request to fetch the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const data = JSON.parse(body);

  // Check if the response includes characters
  if (!data.characters || !Array.isArray(data.characters)) {
    console.log('No characters found');
    return;
  }

  // Fetch and display each character name in order
  const characterUrls = data.characters;

  // Function to fetch character name by URL and print it
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  // Use Promise.all to handle all character requests
  Promise.all(characterUrls.map(fetchCharacterName))
    .then((names) => {
	    names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error fetching character names:', error);
    });
});

