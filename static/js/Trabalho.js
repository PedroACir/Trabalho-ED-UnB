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

function atualizarFila() {
    fetch('/get_fila')
        .then(response => response.json())
        .then(data => {
            var filaDisplay = document.getElementById('queueDisplay');
            filaDisplay.innerHTML = '';
            for (var i = 0; i < data.length; i++) {
                var arquivo = document.createElement('p');
                arquivo.textContent = 'Arquivo: ' + data[i].nome_arquivo + ', Prioridade: ' + data[i].prioridade;
                filaDisplay.appendChild(arquivo);
            }
        });
  }

document.querySelector('.buttonAdd').addEventListener('click', function() {
   var nome_arquivo = document.getElementById('fileInput').value;
   var cargo = document.getElementById('cargos').value;
   fetch('/adicionar', {
       method: 'POST',
       body: new URLSearchParams({
           'nome_arquivo': nome_arquivo,
           'cargo': cargo
       })
   });
});

document.querySelector('.buttonRemove').addEventListener('click', function() {
   var nome_arquivo = document.getElementById('fileInput').value;
   fetch('/remover', {
       method: 'POST',
       body: new URLSearchParams({
           'nome_arquivo': nome_arquivo
       })
   });
});

atualizarFila();