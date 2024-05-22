#!/usr/bin/node

const request = require('request');

const displayStatusCode = (url) => {
    request(url, (error, response) => {
        if (error) {
            console.error(error);
        } else {
            console.log(`code: ${response.statusCode}`);
        }
    });
};

// Example usage:
const url = 'https://jsonplaceholder.typicode.com/posts/1';
displayStatusCode(url);
