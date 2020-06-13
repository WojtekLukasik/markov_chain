graph = {
    # punkt początkowy, punkt końcowy, prawdopodobieństwo przejścia 
    # Ziemia = 1
    # Człowiek = 2
    # Kot = 3
    # Pies = 4
    # Krowa = 5
    # Ptak = 6
    1 : {1 : 0.1, 2 : 0.1, 4 : 0.4, 3 : 0.4},
    2 : {2 : 1.0},
    3 : {3 : 0.1, 1 : 0.5, 5 : 0.4},
    4 : {4 : 0.3, 1 : 0.2, 5 : 0.5},
    5 : {5 : 0.5, 3 : 0.1, 4 : 0.2, 6 : 0.2},
    6 : {6 : 0.8, 5 : 0.2}
}



