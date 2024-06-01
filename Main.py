if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente
    tree = BinaryTree() # Cria uma instância da árvore binária
    N = int(input("Digite o número de elementos da árvore: ").strip().lower())  # Define o número de elementos que serão inseridos na árvore
    dados = [] # Inicializa uma lista vazia para armazenar os dados de entrada

    # Loop para coletar N valores do usuário
    for i in range(N):
        dados.append(int(input(f"Digite o valor {i + 1}: "))) # Adiciona cada valor digitado na lista 'dados'

    # Loop para inserir cada valor na árvore binária
    for val in dados:
        tree.inserir(val) # Insere o valor na árvore

    # Solicita ao usuário o tipo de busca desejado
    tipoBusca = input("\nDigite o tipo de busca desejado (preOrdem, emOrdem, posOrdem): ").strip().lower()

    # Verifica o tipo de busca e executa a busca correspondente
    if tipoBusca == 'pre':
        print("\nPré Ordem:")
        tree.preorder(tree.root) # Realiza a busca em pré-ordem
    elif tipoBusca == 'em':
        print("\nEm Ordem:")
        tree.inorder(tree.root) # Realiza a busca em ordem
    elif tipoBusca == 'pos':
        print("\nPós Ordem:")
        tree.postorder(tree.root) # Realiza a busca em pós-ordem
    else:
        print("Tipo de busca inválido, tente novamente.") # Mensagem de erro para tipo de busca inválido
