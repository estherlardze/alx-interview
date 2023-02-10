async function fetchPlanets() { 
  let results = await fetct("https://swapi-api.alx-tools.com/api/");
  const data = await results.json();
    
  const planets = data.results;
  planets.forEach(item => console.log(item))
  
} 
fetchPlanets();
