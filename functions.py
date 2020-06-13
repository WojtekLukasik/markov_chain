from random import choice
from time import sleep
from graph import graph

states = ['Ziemia', 'Człowiek', 'Kot', 'Pies', 'Krowa', 'Ptak']

def create_transition_matrix(graph):
    transition_matrix = []
    for _ in range(len(graph)):
        transition_matrix.append([])

    for key in graph:
        keys = graph[key].keys()
        for key2 in graph:
            if key2 in keys:
                transition_matrix[key - 1].append(graph[key][key2])
            else:
                transition_matrix[key - 1].append(0.0)


    return transition_matrix

def multiply_matrices(matrix1, matrix2):
    matrix = []
    for x in range(len(matrix1)):
        matrix.append([])
        for y in range(len(matrix1[x])):
            number = 0
            for z in range(len(matrix2[y])):
                number += round(matrix1[x][z] * matrix2[z][y], 7)
            matrix[x].append(number)
    
    return matrix

def matrix_power(matrix, pow):
    result = matrix.copy()
    for _ in range(pow - 1):
        result = multiply_matrices(result, matrix)
    return result

def choose_transition(graph, state):
    matrix = create_transition_matrix(graph)
    possible_states = []

    for x in range(len(matrix[state - 1])):
        iterations = int(matrix[state - 1][x] * 10)
        for _ in range(iterations):
            possible_states.append(x + 1)
    
    return choice(possible_states)


def simulation(graph, starting_state):
    current_state = starting_state
    
    for _ in range(500):
        current_state = choose_transition(graph, current_state)

    return states[current_state - 1]


for x in range(1,51):
    print("Wynik symulacji numer: " + str(x) + " to: " + simulation(graph, 1))
    sleep(0.5)

# matrix1 = [
#     [0.16666, 0.16666, 0.16666, 0.16666, 0.16666, 0.16666]   
# ]

# matrix2 = create_transition_matrix(graph)

# for x in range(1000):
#     matrix = multiply_matrices(matrix1, matrix_power(matrix2, x))
#     print(matrix)

# for x in matrix:
#     print(x)


