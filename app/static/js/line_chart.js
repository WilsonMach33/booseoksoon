// set chart dimensions
var width = 1000,
    height = 500,
    margin = { top: 20, right: 20, bottom: 300, left: 50 };

// set up song data
const songdata=[];

for(let i=0; i<songs.length/2;i++){
    const a = {xvalue: songs[i], yvalue: songs[songs.length/2+i]};
    songdata.push(a);
}

//function
function LineChart(data){
  // create SVG and make it hold chart
  var svg = d3.select("#chart")
    .attr("width", width)
    .attr("height", height);

  var chart = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // make x scale with d.xvalue as domain (range = width)
  var x = d3.scaleBand()
    .domain(data.map(function(d) { return d.xvalue; }))
    .range([0, width - margin.left - margin.right])
    .padding(0.1);

  // make y scale with d.yvalue as [0,max y.value] (range = height)
  var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return d.yvalue; })])
    .range([height - margin.top - margin.bottom, 0])
    .nice();

  // make x axis
  chart.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + (height - margin.top - margin.bottom) + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
      .attr("y", -5)
      .attr("x", -130)
      .style("text-anchor", "middle")
      .attr("transform", "rotate(-90)")

  // make y axis
  chart.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(y).ticks(5))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Popularity");

  // draw horizontal lines for each y-axis tick
  chart.append("g")
    .attr("class", "grid")
    .call(d3.axisLeft(y)
      .tickSize(-width+75)
      .tickFormat("")
    )

  // draw vertical lines for each x-axis tick
  chart.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + (height-50) + ")")
    .call(d3.axisBottom(x)
      .tickSize(-height+50)
      .tickFormat("")
    )

  // add the line to the chart (line chart line)
  var line = d3.line()
    .x(function(d) { return x(d.xvalue) + x.bandwidth() / 2; })
    .y(function(d) { return y(d.yvalue); });

  // add line to chart
  chart.append("path")
    .datum(data)
    .attr("class", "line")
    .attr("d", line);
}

// funtion test
// LineChart(songdata);
console.log(songdata);