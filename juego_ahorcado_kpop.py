import random

#Listado de palabras o nombres para el juego (artistas Kpop)
Lista_nombres=["jungkook", "heeseung","tae", "soobin", "san"]

#Elegir un artista al azar
nombre_secreto= random.choice(Lista_nombres)

letras_usadas=[]
errores=0
num_errores_max=6

#Dibujo del ahorado
ahorcado=[
  """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Bienvenidos al juego del ahorcado version artistas Kpop")

while errores< num_errores_max:
    nombre_mostrado=""

    for letra in nombre_secreto:
        if letra in letras_usadas:
            nombre_mostrado+=letra+""
        else:
            nombre_mostrado +="_"
    
    print("\n palabra:", nombre_mostrado)
    print("Letras usadas:", " , ".join(letras_usadas))

    print(ahorcado[errores])

    if "_" not in nombre_mostrado:
        print("FELICIDADES! \n ADIVINASTE AL ARTISTA")
        break
    
    intento=input("Agrega una letra por favor: ").lower()

    if intento in letras_usadas:
        print("Ups, esa letra ya la usaste")
        continue
    
    letras_usadas.append(intento)

    if intento not in nombre_secreto:
        errores+=1
        print("Ay, esa no era. Errores:", errores)

else:
    print("Oh no, perdiste :(. La palabra era:",nombre_secreto)