// set up song data

// length
const lengthdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[9+i*11]};
    lengthdata.push(a);
}

// popularity data
const poppdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[1+9+i*11]};
    poppdata.push(a);
}

// danceability data
const dancedata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[2+9+i*11]};
    dancedata.push(a);
}

// acousticness data
const acousticnessdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[3+9+i*11]};
    acousticnessdata.push(a);
}

// energy data
const energydata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[4+9+i*11]};
    energydata.push(a);
}

// liveness data
const livenessdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[6+9+i*11]};
    livenessdata.push(a);
}

// loudness data
const loudnessdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[7+9+i*11]};
    loudnessdata.push(a);
}

// speechinesss data
const speechinessdata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[8+9+i*11]};
    speechinessdata.push(a);
}

// valence data
const valencedata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[9+9+i*11]};
    valencedata.push(a);
}

// tempo data
const tempodata = [];
for(let i=0; i<9; i++){
    const a = {xvalue: songs[i], yvalue: songs[10+9+i*11]};
    tempodata.push(a);
}

// set chart dimensions
var width = 1000,
  height = 500,
  margin = { top: 20, right: 20, bottom: 250, left: 50 };

function LineChart(data, chart_id, chart_title){
  // Create the SVG element and append a group element to hold the chart
  var svg = d3.select(chart_id)
    .attr("width", width)
    .attr("height", height);

  var chart = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // Define the x-scale as an ordinal scale with the song titles as domain values
  var x = d3.scaleBand()
    .domain(data.map(function(d) { return d.xvalue; }))
    .range([0, width - margin.left - margin.right])
    .padding(.1);

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
      .attr("x", -100)
      .style("text-anchor", "middle")
      .attr("transform", "rotate(-90)")

  // Add the y-axis to the chart
  chart.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(y).ticks(5))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("x", -6)
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(chart_title);

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

  // Add chart title
  svg.append("text")
    .attr("x", (width + margin.left + margin.right) / 2)
    .attr("y", margin.top / 2)
    .attr("text-anchor", "middle")
    .style("font-size", "14px")
    .style("fill", "red")
    .text(chart_title + " Data Line Chart");

  // Add the line to the chart
  var line = d3.line()
    .x(function(d) { return x(d.xvalue) + x.bandwidth() / 2; })
    .y(function(d) { return y(d.yvalue); });

  chart.append("path")
    .datum(data)
    .attr("class", "line")
    .attr("d", line);
}

LineChart(lengthdata, "#chart1", "Length");
LineChart(poppdata, "#chart2", "Popularity");
LineChart(dancedata, "#chart3", "Danceability");
LineChart(acousticnessdata, "#chart4", "Acousticness");
LineChart(energydata, "#chart5", "Energy");
LineChart(livenessdata, "#chart6", "Liveness");
LineChart(loudnessdata, "#chart7", "Loudness");
LineChart(speechinessdata, "#chart8", "Speechiness");
LineChart(valencedata, "#chart9", "Valence");
LineChart(tempodata, "#chart10", "Tempo");



// console.log(poppdata);
// console.log(songs);