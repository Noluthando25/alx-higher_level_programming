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
