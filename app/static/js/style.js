//yay

var getImage = function(event) {
    var image = document.getElementById("profile-pic");
    image.src = URL.createObjectURL(event.target.files[0]);
};
