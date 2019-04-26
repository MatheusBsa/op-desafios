#! python3

# Primos em Pi - Matheus Barbosa Souza


import math
import sys


def fast_prime(number):
    """Função de retorno rápido de números primos"""
    if number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    maiorraiz = int(math.ceil(math.sqrt(number)))
    # Recebe o maior valor da raiz quadrada do numero

    for i in range(3, maiorraiz, 2):
        if number % i == 0:
            return False

    return True


def insert_prime(sequence):
    """Insere todos os primos na lista"""
    numbers = sequence[2:]  # Ignore '3.'
    entire_sequence = ''
    list_sequence = []


    i = 0
    while i < len(numbers)-1: 
           
        if fast_prime(int(numbers[i:4+i])):
            entire_sequence += numbers[i:4+i]
            i += 3
        elif fast_prime(int(numbers[i:3+i])):
            entire_sequence += numbers[i:3+i]
            i += 2
        elif fast_prime(int(numbers[i:2+i])):
            entire_sequence += numbers[i:2+i]
            i += 1
        elif fast_prime(int(numbers[i:1+i])):
            entire_sequence += numbers[i:1+i]
        elif not fast_prime(int(numbers[i:i+1])):
            list_sequence.append(entire_sequence)
            i += 1
        i += 1
        
    return list_sequence

pi_file = sys.argv[1]
with open(pi_file) as file:
    sequence = file.read()
    print(insert_prime(sequence))