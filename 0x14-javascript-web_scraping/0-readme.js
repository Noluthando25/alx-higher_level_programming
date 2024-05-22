#!/usr/bin/node

const fs = require('fs');
// Import the built in node.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
	// Use fs.readFile
	// 'utf8' specifies the encoding of the file being read

    if (error) {
	    // An error message will be shown.
	    console.error('Error occurred while reading the file:', error);
    } else {
	    // If successful it will contain the content of the file
	    console.log(content);
    }
});
