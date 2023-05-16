const Questions = [{
        id: 1,
        q: "danceability",
        a: [{text: "click me", danceability: 0.58 },
            {text: "no", danceability: 0},
            {text: "no", danceability: 0},
            {text: "no", danceability: 0}
        ]
    },
    {
        id: 2,
        q: "acousticness",
        a: [{text: "click me", acousticness: 0.575 },
            {text: "no", acousticness: 0},
            {text: "no", acousticness: 0},
            {text: "no", acousticness: 0}
        ]
    },
    {
        id: 3,
        q: "energy",
        a: [{text: "click me", energy: 0.491 },
            {text: "no", energy: 0},
            {text: "no", energy: 0},
            {text: "no", energy: 0}
        ]
    },
    {
        id: 4,
        q: "liveness",
        a: [{text: "click me", liveness: 0.121 },
            {text: "no", liveness: 0},
            {text: "no", liveness: 0},
            {text: "no", liveness: 0}
        ]
    }
]

var start = true;

function iterate(id) {
    //code here
}

if (start) {
    iterate("0");
}
 
// Next button and method
const next = document.getElementsByClassName('next')[0];
var id = 0;
 
next.addEventListener("click", () => {
    start = false;
    if (id < 2) {
        id++;
        iterate(id);
        console.log(id);
    }
 
})