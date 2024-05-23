if __name__ == "__main__":
    tree = BinaryTree()
    N = 8
    dados = []
    for i in range(N):
        dados.append(int(input(f"Digite o valor {i + 1}: ")))
    for val in dados:
        tree.insert(val)

    tipoBusca = input("\nDigite o tipo de busca desejado (pre, em, pos): ").strip().lower()
    if tipoBusca == 'pre':
        print("\nPré Ordem:")
        tree.preorder(tree.root)
    elif tipoBusca == 'em':
        print("\nEm Ordem:")
        tree.inorder(tree.root)
    elif tipoBusca == 'pos':
        print("\nPós Ordem:")
        tree.postorder(tree.root)
    else:
        print("Tipo de busca inválido, tente novamente.")
