#!/usr/bin/node

async function fetchPlanets(id) { 
  let results = await fetct(`https://swapi-api.alx-tools.com/api/people/${id}`);
  const data = await results.json();
    
  const planets = data.results;
  planets.forEach(item => console.log(item.name))
  
} 
fetchPlanets();
