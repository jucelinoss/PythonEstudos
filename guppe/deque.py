"""
Módulo Collections - Deque
- lista de alta performance

"""
from collections import deque

deq = deque('geek')


print(deq)

# Add elementos ao deque
deq.append('y')
deq.appendleft('k')
# add no começo da lista

print(deq)

# Remover elementos ao deque
print(deq.pop())     # remove e retorna o ultimo elemento

print(deq)
# remove e retorna o primeiro elemento
print(deq.popleft())

print(deq)



