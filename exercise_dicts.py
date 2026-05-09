# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    inventario = {}

    for item in items:
        if item in inventario:
            inventario[item] = inventario[item] + 1
        else:
            inventario[item] = 1

    return inventario

def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    for item in items:
        # Si el ítem ya existe, incrementamos su valor
        if item in inventario:
            inventario[item] = inventario[item] + 1
        # Si no existe, lo agregamos empezando en 1
        else:
            inventario[item] = 1

    return inventario

def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    for item in items:
        # Solo procesamos si el ítem existe en el inventario
        if item in inventario:
            # Si la cantidad es mayor a 0, restamos 1
            if inventario[item] > 0:
                inventario[item] = inventario[item] - 1
            # Si ya es 0, no hacemos nada (se ignora la solicitud extra)

    return inventario


def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    if item in inventario:
        del inventario[item]

    return inventario

def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    resultado = []

    # .items() nos da la clave y el valor en cada vuelta del for
    for item, cantidad in inventario.items():
        # Solo incluimos los que tienen cantidad mayor a 0
        if cantidad > 0:
            resultado.append((item, cantidad))

    return resultado

def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".

    Args:
        diccionario: Diccionario {nombre: puntaje}

    Returns:
        String con la clave de mayor valor, o "" si el dict está vacío

    Ejemplo:
        find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}) -> 'Emma'
    """
    if len(diccionario) == 0:
        return ""

    nombre_maximo = ""
    puntaje_maximo = -1  # Empezamos con un valor muy bajo

    for nombre, puntaje in diccionario.items():
        # Si el puntaje actual es mayor al récord que teníamos
        if puntaje > puntaje_maximo:
            puntaje_maximo = puntaje
            nombre_maximo = nombre

    return nombre_maximo

def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido

    Ejemplo:
        reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        -> {1: 'a', 2: 'be', 3: 'cd'}
    """
    invertido = {}

    # Recorremos cada par clave-valor
    for clave, valor in diccionario.items():
        # Si el valor ya existe como clave en nuestro nuevo dict, concatenamos
        if valor in invertido:
            invertido[valor] = invertido[valor] + clave
        # Si no existe, lo creamos con la clave actual como string
        else:
            invertido[valor] = clave

    return invertido


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    if not palabras:
        return {}

    frecuencia = {}
    for p in palabras:
        # Si la palabra ya está, sumamos 1 al contador
        if p in frecuencia:
            frecuencia[p] = frecuencia[p] + 1
        # Si es la primera vez que aparece, inicializamos en 1
        else:
            frecuencia[p] = 1

    return frecuencia


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    if not gastos:
        return ""

    mejor_categoria = ""
    max_promedio = -1.0  # Empezamos con un valor bajo para la comparación

    for categoria, lista_gastos in gastos.items():
        # Calculamos el promedio: suma de gastos dividido la cantidad
        if len(lista_gastos) > 0:
            promedio_actual = sum(lista_gastos) / len(lista_gastos)
        else:
            promedio_actual = 0

        # Si este promedio es mayor al máximo que teníamos guardado
        if promedio_actual > max_promedio:
            max_promedio = promedio_actual
            mejor_categoria = categoria

    return mejor_categoria

def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    totales = {}

    # Recorremos cada categoría y su lista de montos
    for categoria, lista_montos in gastos.items():
        # Usamos la función sum() de Python para sumar la lista completa
        totales[categoria] = sum(lista_montos)

    return totales


def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    resultado = {}

    # 1. Primer bucle: entramos en cada categoría (Food, Transport, etc.)
    for categoria, lista_tuplas in gastos.items():

        # 2. Segundo bucle: recorremos la lista de tuplas de esa categoría
        for tipo, monto in lista_tuplas:

            # 3. Agrupamos por tipo en el nuevo diccionario
            if tipo in resultado:
                resultado[tipo] = resultado[tipo] + monto
            else:
                resultado[tipo] = monto

    return resultado
