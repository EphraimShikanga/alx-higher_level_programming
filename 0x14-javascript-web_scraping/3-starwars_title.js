const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, body);
  } else {
    const movieData = JSON.parse(body);
    console.log('Title:', movieData.title);
  }
});
