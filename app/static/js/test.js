var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle"); 
var stopButton = document.getElementById("buttonStop"); 

var ctx = c.getContext("2d");

ctx.fillStyle = "#3EB489";

var requestID = "stop";

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    window.cancelAnimationFrame(requestID);
    clear();

    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();
    if (growing) {
        if (radius < 250) {
            radius = radius+1;
        }
        else { growing = false; }
    } else {
        if (radius > 0) {
            radius = radius-1;
        }
        else { growing = true; }
    }
    requestID = window.requestAnimationFrame(drawDot);

};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);