// set chart dimensions
var width = 1000,
  height = 500,
  margin = { top: 20, right: 20, bottom: 300, left: 50 };

// set up song data
var column = ["length", "popularity", "danceability", "acousticness", 
"energy", "instrumentalness", "liveness", "loudness", 
"speechiness", "valence","tempo"]

var album = ["Taylor Swift", "Speak Now (Deluxe Package)", "Red (Deluxe Edition)",
"1989 (Deluxe)", "reputation", "Lover", "folklore (deluxe version)",
"evermore (deluxe version)", "Fearless (Taylor's Version)"]

const songdata=[];
for(int i=0; i<column.length; i++){
  songdata+=[]
}
  
// for(let i=0; i<9; i++){
//     const a = {xvalue: songs[i], yvalue: songs[9+i*11]};
//     lengthdata.push(a);
// }

//function
function LineChart(data){
  // Create the SVG element and append a group element to hold the chart
  var svg = d3.select("#chart")
    .attr("width", width)
    .attr("height", height);

  var chart = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // Define the x-scale as an ordinal scale with the song titles as domain values
  var x = d3.scaleBand()
  .domain(data.map(function(d) { return d.xvalue; }))
  .range([0, width - margin.left - margin.right])
  .padding(0.1);

  // Define the y-scale as a linear scale with the maximum popularity value as the domain
  var y = d3.scaleLinear()
  .domain([0, d3.max(data, function(d) { return d.yvalue; })])
  .range([height - margin.top - margin.bottom, 0])
  .nice();

  // Add the x-axis to the chart
  chart.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + (height - margin.top - margin.bottom) + ")")
  .call(d3.axisBottom(x))
  .selectAll("text")
    .attr("y", -5)
    .attr("x", -130)
    .style("text-anchor", "middle")
    .attr("transform", "rotate(-90)")

  // Add the y-axis to the chart
  chart.append("g")
  .attr("class", "y axis")
  .call(d3.axisLeft(y).ticks(5))
  .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Popularity");

  // Draw horizontal lines for each y-axis tick
  chart.append("g")
  .attr("class", "grid")
  .call(d3.axisLeft(y)
    .tickSize(-width+75)
    .tickFormat("")
  )

  // Draw vertical lines for each x-axis tick
  chart.append("g")
  .attr("class", "grid")
  .attr("transform", "translate(0," + (height-50) + ")")
  .call(d3.axisBottom(x)
    .tickSize(-height+50)
    .tickFormat("")
  )

  // Add the line to the chart
  var line = d3.line()
  .x(function(d) { return x(d.xvalue) + x.bandwidth() / 2; })
  .y(function(d) { return y(d.yvalue); });

  chart.append("path")
  .datum(data)
  .attr("class", "line")
  .attr("d", line);
}

// LineChart(songdata);
console.log(lengthdata);
console.log(songs)