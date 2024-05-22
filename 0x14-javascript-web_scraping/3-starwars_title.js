#!/usr/bin/node

const request = require('request');

const getMovieTitle = (movieId) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

    request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const movie = JSON.parse(body);
            console.log(`Title of Episode ${movie.episode_id}: ${movie.title}`);
        } else {
            console.error('Error fetching movie data:', error);
        }
    });
};

const movieId = 1; // Specify the movie ID here
getMovieTitle(movieId);
