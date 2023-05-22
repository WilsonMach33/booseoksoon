var dance_slider = document.getElementById("dance_range");
var dance_output = document.getElementById("dance_value");

var acoust_slider = document.getElementById("acoust_range");
var acoust_output = document.getElementById("acoust_value");

var energy_slider = document.getElementById("energy_range");
var energy_output = document.getElementById("energy_value");

var live_slider = document.getElementById("live_range");
var live_output = document.getElementById("live_value");

dance_output.innerHTML = dance_slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
dance_slider.oninput = function() {
  dance_output.innerHTML = this.value;
}

acoust_slider.oninput = function() {
    acoust_output.innerHTML = this.value;
  }

energy_slider.oninput = function() {
  energy_output.innerHTML = this.value;
}

live_slider.oninput = function() {
    live_output.innerHTML = this.value;
}


