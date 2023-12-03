from time import sleep

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Noh:
    def __init__(self, documento, prioridade, nome_arquivo):
        # Criação de um nó com as informações do documento, prioridade e nome do arquivo.
        self.documento = documento
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None
        self.nome_arquivo = nome_arquivo

class Imprimir:
    def __init__(self):
        # Inicializa a classe de gerenciamento de impressão.
        self.primeiro = None
        self.ultimo = None

    def criar_noh(self, nome, prioridade):
        try:
            # Tenta abrir o arquivo e ler seu conteúdo.
            with open(nome, 'r') as arquivo:
                conteudo = arquivo.read()
                # Cria um novo nó com o conteúdo do arquivo, prioridade e nome do arquivo.
                novo_Noh = Noh(conteudo, prioridade, nome)  
                return novo_Noh
        except FileNotFoundError:
            # Para caso o arquivo não for encontrado, imprime uma mensagem de erro.
            print(f'O Arquivo {nome} não foi encontrado :(')
            return None

    def adicionar_na_fila(self, novo_Noh, prioridade):
        if self.primeiro is None:
            # Se a fila estiver vazia, adiciona o novo nó como o primeiro e último
            self.primeiro = novo_Noh
            self.ultimo = novo_Noh
            print(f'Um novo documento {novo_Noh.nome_arquivo} entrou na fila')
        else:
            # Se a fila não estiver vazia, adiciona o novo nó na posição correta
            atual = self.primeiro
            while atual is not None and atual.prioridade >= prioridade:
                atual = atual.proximo

            if atual is None:
                # Adiciona o novo nó no final da fila
                self.ultimo.proximo = novo_Noh
                novo_Noh.anterior = self.ultimo
                self.ultimo = novo_Noh
            elif atual.anterior is None:
                # Se o novo nó for o mais prioritário, adiciona no início da fila
                novo_Noh.proximo = self.primeiro
                self.primeiro.anterior = novo_Noh
                self.primeiro = novo_Noh
            else:
                # Adiciona o novo nó no meio da fila
                novo_Noh.proximo = atual
                novo_Noh.anterior = atual.anterior
                atual.anterior.proximo = novo_Noh
                atual.anterior = novo_Noh
            print(f'Um novo documento {novo_Noh.nome_arquivo} entrou na fila!!')

    def adiciona(self, nome, prioridade):
        # Adiciona um novo documento à fila de impressão.
        novo_Noh = self.criar_noh(nome, prioridade)
        if novo_Noh:
            self.adicionar_na_fila(novo_Noh, prioridade)

    def imprime(self):
        if self.primeiro is None:
            # Se não houver arquivos para imprimir, exibe uma mensagem.
            print("Não há arquivos!!")
            return
        atual = self.primeiro
        while atual is not None:
            sleep(0.5)
            print(f'Imprimindo o arquivo {atual.nome_arquivo}, aguarde...')
            atual = atual.proximo
            if atual == self.primeiro:
                break

    def organiza(self):
        if self.primeiro is None:
            # Se não houver documentos na fila, exibe uma mensagem.
            print('Não há documentos!!')
            return
        print('Arquivos na fila:')
        atual = self.primeiro
        while atual is not None:
            # Exibe informações sobre os documentos na fila.
            print(f'Grau de prioridade: {atual.prioridade}\n'
                  f'Tamanho: O arquivo possui {len(atual.documento)} caracteres')
            atual = atual.proximo

            if atual == self.primeiro:
                break

gerenciador = Imprimir()

@app.route('/')
def home():
    return render_template('Trabalho.html')

@app.route('/add_to_queue', methods=['POST'])
def add_to_queue():
 data = request.get_json()
 text = data['text']
 cargo = data['cargo']
 gerenciador.adiciona(text, cargo)
 return jsonify({'status': 'success'})