def outroCaminhoMinimo(A,x,n):
  d = [float('inf')] * n
  s = [None] * n
  d[x] = 0

  for z in range(n):
        if z != x:
            d[z] = A[x][z]
            s[z] = x

    # Encontra os caminhos mínimos de comprimentos 2, 3, etc.
  for i in range(2, n):
      t = d[:]  # Copia o vetor d corrente em t
      
      # Altera t a fim de guardar os menores caminhos de comprimento i
      for z in range(n):
          if z != x:
              p = -1
              for p_temp in range(n):
                  if p_temp != z and d[p_temp] + A[p_temp][z] < t[z]:
                      p = p_temp
                      t[z] = d[p_temp] + A[p_temp][z]
              if p != -1:
                  s[z] = p
      
      d = t[:]  # Copia t de volta para d

  return d, s
'''
# Exemplo de uso
A = [
    [0, 1, 4, float('inf')],
    [float('inf'), 0, 4, 2],
    [float('inf'), float('inf'), 0, 3],
    [float('inf'), float('inf'), float('inf'), 0]
]
x = 0
n = 4

distancias, predecessores  = outroCaminhoMinimo(A, x, n)
print("Distâncias:", distancias)
print("Predecessores:", predecessores )
'''
