from collections import deque
from posixpath import join

# Define uma função para realizar uma busca em profundidade em um grafo a partir de um vértice inicial.
def busca_profundidade(grafo, vertice_inicial):
  visitados = set() # Conjunto para rastrear os vértices visitados
  pilha = [vertice_inicial]  # Pilha para gerenciar os vértices a serem explorados, iniciando com o vértice inicial

  while pilha: # Continua enquanto houver vértices na pilha
      vertice_atual = pilha.pop() # Remove o último vértice da pilha (último a ser adicionado)
      if vertice_atual not in visitados: # Verifica se o vértice ainda não foi visitado
          visitados.add(vertice_atual) # Marca o vértice como visitado
          # Adiciona os vizinhos não visitados do vértice atual na pilha
          for vizinho in grafo[vertice_atual]:
              if vizinho not in visitados:
                  pilha.append(vizinho)

  return visitados # Retorna o conjunto de vértices visitados

def busca_largura(grafo, vertice_inicial):
  # Inicialização
  visitados = {vertice: 0 for vertice in grafo}  # Marca todos os vértices como não visitados (0)
  predecessores = {vertice: None for vertice in grafo}  # Armazena predecessores de cada vértice
  fila = deque([vertice_inicial])
  visitados[vertice_inicial] = 1  # Marca o vértice inicial como visitado (1)

  # Busca em Largura
  while fila:
      u = fila.popleft()  # Desenfileira o primeiro vértice
      for v in grafo[u]:  # Para cada vizinho v de u
          if visitados[v] == 0:  # Se v não foi visitado
              visitados[v] = 1  # Marca v como visitado
              predecessores[v] = u  # Define o predecessor de v como u
              fila.append(v)  # Enfileira v

  return visitados # Retorna o conjunto de vértices visitados

def grafo_usuario():
  # Pega o número de vértices e arestas do grafo do usuário
  num_vertices = int(input("Digite o número de vértices do grafo: "))
  num_arestas = int(input("Digite o número de arestas do grafo: "))

  # Cria uma lista de adjacência vazia
  grafo = {}

  # Pega as informações das arestas do grafo do usuário
  for i in range(num_arestas):
    v1, v2 = map(int, input(f"Digite a aresta {i + 1} (v1 v2): ").split())

    # Adiciona as arestas à lista de adjacência
    if v1 not in grafo:
      grafo[v1] = []
    if v2 not in grafo:
      grafo[v2] = []
    grafo[v1].append(v2)
    grafo[v2].append(v1)

  # Pega o vértice inicial da busca do usuário
  vertice_inicial = int(input("Digite o vértice inicial da busca: "))

  # Solicita ao usuário o tipo de busca (profundidade ou largura)
  escolha_busca = (input("\nEntre com o tipo de Busca (profundidade ou largura): ")).strip().lower()

  # Realiza a busca em profundidade se o usuário escolher 'profundidade'
  if escolha_busca == 'profundidade':
    visitadosP = busca_profundidade(grafo, vertice_inicial)
    # Imprime os vértices visitados
    print("Vértices visitados:", visitadosP)
  # Realiza a busca em largura se o usuário escolher 'largura'
  elif escolha_busca == 'largura':
    visitadosL = busca_largura(grafo, vertice_inicial)
    # Imprime os vértices visitados
    print("Vértices visitados:", visitadosL)
  else:
    print("Tipo de busca inválido, tente novamente.")

# Chama a função principal que interage com o usuário e realiza a busca no grafo
grafo_usuario()
