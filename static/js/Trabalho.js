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

document.querySelector('.buttonAdd').addEventListener('click', function() {
    var fileInput = document.querySelector('#fileInput');
    var cargoInput = document.querySelector('#cargos');
    var text = fileInput.value;
    var cargo = cargoInput.value;
  
    fetch('/add_to_queue', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text, cargo: cargo })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Atualiza a div queueDisplay com a fila atualizada
            var queueDisplay = document.querySelector('#queueDisplay');
            queueDisplay.textContent = gerenciador.organiza();
        }
    });
  });