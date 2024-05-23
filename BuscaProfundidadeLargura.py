#**BUSCA PROFUNDIDADE**
def busca_profundidade(grafo, vertice_inicial):
  visitadosP = set()
  pilha = [vertice_inicial]

  while pilha:
    vertice_atual = pilha.pop()
    if vertice_atual not in visitadosP:
      visitadosP.add(vertice_atual)
      for vizinho in grafo[vertice_atual]:
        if vizinho not in visitadosP:
          pilha.append(vizinho)
  return visitadosP

#**BUSCA LARGURA**
def busca_largura(grafo, vertice_inicial):
  visitadosL = set()
  fila = [vertice_inicial]

  while fila:
    vertice_atual = fila.pop(0)
    if vertice_atual not in visitadosL:
      visitadosL.add(vertice_atual)
      for vizinho in grafo[vertice_atual]:
        if vizinho not in visitadosL:
          fila.append(vizinho)
  return visitadosL

def grafo_usuario():
  # Pega o número de vértices e arestas do grafo do usuário
  num_vertices = int(input("Digite o número de vértices do grafo: "))
  num_arestas = int(input("Digite o número de arestas do grafo: "))

  # Cria uma lista de adjacência vazia
  grafo = {}

  # Pega as informações das arestas do grafo do usuário
  for i in range(num_arestas):
    v1, v2 = map(int, input(f"Digite a aresta {i + 1} (v1, v2): ").split())

    # Adiciona as arestas à lista de adjacência
    if v1 not in grafo:
      grafo[v1] = []
    if v2 not in grafo:
      grafo[v2] = []
    grafo[v1].append(v2)
    grafo[v2].append(v1)

  # Pega o vértice inicial da busca do usuário
  vertice_inicial = int(input("Digite o vértice inicial da busca: "))

  # Realiza a busca em profundidade e largura
  visitadosP = busca_profundidade(grafo, vertice_inicial)
  visitadosL = busca_largura(grafo, vertice_inicial)

  escolha_busca = (input("\nEntre com o tipo de Busca (profundidade ou largura): ")).strip().lower()

  if escolha_busca == 'profundidade':
    # Imprime os vértices visitados
    print("Vértices visitados:", visitadosP)
  elif escolha_busca == 'largura':
    # Imprime os vértices visitados
    print("Vértices visitados:", visitadosL)
  else:
    print("Tipo de busca inválido, tente novamente.")

grafo_usuario()
