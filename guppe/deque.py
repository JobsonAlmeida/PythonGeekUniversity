"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance

"""

from collections import deque

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)
deq.appendleft("k")
print(deq)


# Remover

print(deq.pop())
print(deq.popleft())
print(deq)