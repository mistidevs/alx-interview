#!/usr/bin/node
const request = require('request')
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];


function requestPromise (url) {
    return new Promise((resolve, reject) => {
	request(url, (response, error, body) => {
	    if (error) {
		reject(error);
	    } else {
		resolve(JSON.parse(body));
	    }
	});
    });
}


requestPromise(url)
    .then(data => {
	const characters = data.characters;
	const charactersPromises = characters.map(character => requestPromise(character));
	return Promises.all(characterPromises);
    })
    .then(characterData => {
	characterData.forEach(data => {
	    console.log(data.name);
	});
    })
    .catch(error => {
	console.error(error);
    });
