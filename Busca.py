import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def cirar_No(self, data):
        return Node(data)
    
    def inserir(self, data):
        if self.root is None:
            self.root = self.cirar_No(data)
        else:
            self._inserir(data, self.root)
    
    def _inserir(self, data, no_atual):
        if data < no_atual.data:
            if no_atual.left is None:
                no_atual.left = self.cirar_No(data)
            else:
                self._inserir(data, no_atual.left)
        elif data > no_atual.data:
            if no_atual.right is None:
                no_atual.right = self.cirar_No(data)
            else:
                self._inserir(data, no_atual.right)
        else:
            print("Valor já existe na Árvore!")
    
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
