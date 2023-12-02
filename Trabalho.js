var open_modal = document.getElementById("open_modal"); 

var modal = document.getElementById("modal_1"); 

var close_modal = document.getElementsByClassName("close_modal")[0];

open_modal.onclick = function () {
    modal.style.display = "flex";
};

close_modal.onclick = function () {
    modal.style.display = "none";
};

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
