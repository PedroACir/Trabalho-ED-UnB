from time import sleep

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Node:
    def __init__(self, nome_arquivo, prioridade):
        self.nome_arquivo = nome_arquivo
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

    def get_saida(self):
       return {'nome_arquivo': self.nome_arquivo, 'prioridade': self.prioridade}

class FilaImpressao:
    def __init__(self):
       self.primeiro = None
       self.ultimo = None
       self.cargos = {'presidente': 1, 'assessor': 2, 'trainee': 3}

    def adicionar(self, nome_arquivo, cargo):
        prioridade = self.cargos[cargo]
        novo_noh = Node(nome_arquivo, prioridade)
        if self.primeiro is None or self.primeiro.prioridade > prioridade:
           novo_noh.proximo = self.primeiro
           if self.primeiro is not None:
               self.primeiro.anterior = novo_noh
           self.primeiro = novo_noh
           if self.ultimo is None:
                self.ultimo = novo_noh
        else:
           atual = self.primeiro
           while atual.proximo is not None and atual.proximo.prioridade <= prioridade:
               atual = atual.proximo
           novo_noh.proximo = atual.proximo
           if atual.proximo is not None:
               atual.proximo.anterior = novo_noh
           atual.proximo = novo_noh
           novo_noh.anterior = atual
           if novo_noh.proximo is None:
               self.ultimo = novo_noh

    def remover(self, nome_arquivo):
       if self.primeiro is None:
           print("Não há arquivos na fila para remover.")
           return
       if self.primeiro.nome_arquivo == nome_arquivo:
           self.primeiro = self.primeiro.proximo
           if self.primeiro is not None:
               self.primeiro.anterior = None
           if self.primeiro is None:
               self.ultimo = None
       else:
           atual = self.primeiro
           while atual.proximo is not None and atual.proximo.nome_arquivo != nome_arquivo:
               atual = atual.proximo
           if atual.proximo is not None:
               atual.proximo = atual.proximo.proximo
               if atual.proximo is not None:
                   atual.proximo.anterior = atual
               if atual.proximo is None:
                   self.ultimo = atual
    def imprimir(self):
       atual = self.primeiro
       while atual is not None:
           print(f'Imprimindo o arquivo {atual.nome_arquivo}, aguarde...')
           atual = atual.proximo


fila = FilaImpressao()

@app.route('/')
def home():
    return render_template('Trabalho.html')
@app.route('/adicionar', methods=['POST'])
def adicionar():
   nome_arquivo = request.form['nome_arquivo']
   cargo = request.form['cargo']
   fila.adicionar(nome_arquivo, cargo)
   return jsonify({'status': 'success'})

@app.route('/remover', methods=['POST'])
def remover():
   nome_arquivo = request.form['nome_arquivo']
   fila.remover(nome_arquivo)
   return jsonify({'status': 'success'})

@app.route('/get_fila', methods=['GET'])
def get_fila():
  fila_json = []
  atual = fila.primeiro
  while atual is not None:
      fila_json.append(atual.get_saida())
      atual = atual.proximo
  return jsonify(fila_json)