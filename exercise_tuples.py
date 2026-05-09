# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    #Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)
    """

    return registro[1]



def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """
    return coordenada[0], coordenada[1]


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.

    - Registro de Azara: (tesoro, coordenada) -> ej: ('Brass Spyglass', '4B')
    - Registro de Rui: (ubicacion, coordenada, cuadrante) ->
      ej: ('Abandoned Lighthouse', ('4', 'B'), 'Blue')

    Si las coordenadas coinciden, retornar una tupla combinada:
    (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    Si NO coinciden, retornar el string "not a match".

    Args:
        registro_azara: Tupla (tesoro, coordenada)
        registro_rui: Tupla (ubicacion, coordenada, cuadrante)

    Returns:
        Tupla combinada si las coordenadas coinciden, o "not a match" si no.
    """
    tesoro_azara = registro_azara[0]
    coord_azara_str = registro_azara[1]

    # 2. Convertimos la coordenada de Azara ("4B" -> ("4", "B"))
    # para poder compararla con la de Rui
    coord_azara_tupla = convert_coordinate(coord_azara_str)

    # 3. Extraemos la coordenada de Rui (que está en el índice 1)
    coord_rui = registro_rui[1]

    # 4. Comparamos
    if coord_azara_tupla == coord_rui:
        # Si coinciden, creamos la gran tupla combinada
        # (tesoro, coord_azara, ubicacion, coord_rui, cuadrante)
        return tesoro_azara, coord_azara_str, registro_rui[0], registro_rui[1], registro_rui[2]
    else:
        # Si no coinciden
        return "not a match"


def sum_tuple(numeros):
    """
    Recorre una tupla de números y retorna la suma total.
    Si la tupla está vacía, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo la tupla con un for (o while).

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos de la tupla

    Ejemplo:
        sum_tuple((1, 2, 3, 4, 5)) -> 15
        sum_tuple(()) -> 0
    """

    total = 0

    for n in numeros:
        total = total + n

    return total


def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.

    No se permite usar el método .count(). Implementar el conteo
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos de cualquier tipo
        elemento: El elemento a contar

    Returns:
        La cantidad de veces que aparece el elemento (int)

    Ejemplo:
        count_occurrences((1, 2, 2, 3, 2), 2) -> 3
        count_occurrences(('a', 'b', 'a'), 'c') -> 0
    """
    cantidad = 0

    for item in tupla:
        if item == elemento:
            cantidad = cantidad + 1

    return cantidad

def find_index(tupla, elemento):
    """
    Recorre la tupla y retorna el índice de la PRIMERA aparición del
    elemento. Si el elemento no se encuentra, retorna -1.

    No se permite usar el método .index(). Implementar la búsqueda
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos
        elemento: El elemento a buscar

    Returns:
        El índice (int) de la primera aparición, o -1 si no está

    Ejemplo:
        find_index(('a', 'b', 'c', 'b'), 'b') -> 1
        find_index((1, 2, 3), 9) -> -1
    """
    for i in range(len(tupla)):
        if tupla[i] == elemento:
            return i

    return -1

def filter_positives(numeros):
    """
    Recorre una tupla de números y retorna una nueva tupla con solo
    los números positivos (> 0). El cero NO se considera positivo.

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        Tupla con los números positivos, en el orden original

    Ejemplo:
        filter_positives((-3, 1, 0, 5, -2, 7)) -> (1, 5, 7)
        filter_positives((-1, -2, -3)) -> ()
    """
    positivos_lista = []

    # 2. Recorremos la tupla original
    for n in numeros:
        # 3. Verificamos la condición: que sea mayor a 0
        if n > 0:
            # Agregamos a nuestra lista temporal
            positivos_lista.append(n)

    # 4. Convertimos la lista de vuelta a tupla antes de retornar
    return tuple(positivos_lista)
