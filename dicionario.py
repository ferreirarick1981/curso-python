#!/usr/bin//python3
pessoas =[
    {'nome':'rick', 'idade':37},
    {'nome':'ana luiza','idade':4},
    {'nome': 'nadir', 'idade':63}
    ]

for pessoa in pessoas:
    nome = pessoa['nome']
    idade= pessoa['idade']
    print("O(A){} tem {} anos". format(nome, idade))
    print(".........................")