#!/usr/bin/node

const fs = require('fs');

const writeStringToFile = (filePath, content) => {
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error(err);
        } else {
            console.log('String successfully written to file.');
        }
    });
};
