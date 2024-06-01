import ctypes

# Classe que define um nó da árvore binária
class Node:
    def __init__(self, data):
        self.data = data    # Dado armazenado no nó
        self.left = None    # Referência para o filho esquerdo
        self.right = None   # Referência para o filho direito

# Classe que define a árvore binária
class BinaryTree:
    def __init__(self):
        self.root = None # Inicializa a raiz da árvore como None

    # Método para criar um novo nó
    def cirar_No(self, data):
        return Node(data) # Retorna um novo nó com o dado fornecido

    # Método para inserir um dado na árvore
    def inserir(self, data):
        if self.root is None:
            self.root = self.cirar_No(data) # Se a raiz for None, cria o nó raiz
        else:
            self._inserir(data, self.root) # Caso contrário, chama o método auxiliar para inserir

    # Método auxiliar para inserir um dado na árvore de forma recursiva
    def _inserir(self, data, no_atual):
        if data < no_atual.data:
            if no_atual.left is None:
                no_atual.left = self.cirar_No(data) # Insere à esquerda se não houver filho esquerdo
            else:
                self._inserir(data, no_atual.left) # Caso contrário repete
        elif data > no_atual.data:
            if no_atual.right is None:
                no_atual.right = self.cirar_No(data) # Insere à direita se não houver filho direito
            else:
                self._inserir(data, no_atual.right) # Caso contrário repete
        else:
            print("Valor já existe na Árvore!") # Imprime mensagem se o valor já existir

    # Método para percorrer a árvore em pré-ordem
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")  # Visita o nó
            self.preorder(node.left)   # Percorre a subárvore esquerda
            self.preorder(node.right)  # Percorre a subárvore direita

    # Método para percorrer a árvore em ordem
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)    # Percorre a subárvore esquerda
            print(node.data, end=" ")  # Visita o nó
            self.inorder(node.right)   # Percorre a subárvore direita

    # Método para percorrer a árvore em pós-ordem
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)   # Percorre a subárvore esquerda
            self.postorder(node.right)  # Percorre a subárvore direita
            print(node.data, end=" ")   # Visita o nó
