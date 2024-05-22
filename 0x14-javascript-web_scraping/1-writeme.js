!/usr/bin/node

const fs = require('fs');
// Import the built in node.js

fs.writeFile(process.argv[2], process.argv[3], 'utf8', err => {
	// Write data to a file specified
	// Process.argv[3].

	if (err) {
		// The error perimeter will contain an error message. 
		console.error(err); 
	}
});
