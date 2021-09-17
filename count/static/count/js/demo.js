let arr="{{elementos|safe}}" 
let cadena = arr.replace(/'/g, '"')
console.log("cadena: ", cadena)
myObject = JSON.parse(cadena);
console.log('Objeto Completo: ', myObject)

let movies = [
   {
       title: "Fight Club",
       rank: 10,
       id: "tt0137523"
   },
   {
       title: "The Shawshank Redemption",
       rank: 1,
       id: "tt0111161"
   }
   
]

function displayMovies(movies){
let table = '<table>';
table += '<tr><th>ID</th><th>Name</th><th>Rank</th></tr>';
movies.map((movie, index) => {
   table = table + '<tr>',
   table = table + '<td>' + 'Title:' + `${movie.id}` + '</td>',
   table = table + '<td>' + 'Title:' + `${movie.title}` + '</td>',
   table = table + '<td>' + 'Title:' + `${movie.rank}` + '</td>'
});  
   table += "</table>"
   document.getElementById("movies-list").innerHTML = table;
}

displayMovies(movies);