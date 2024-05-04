def calcular_gematría(letra):
    # Diccionario de correspondencia entre letras y valores de gematría para el alfabeto hebreo
    gematría_hebrea = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ך': 500, 'ל': 30, 'מ': 40, 'ם': 600, 'נ': 50, 'ן': 700,
        'ס': 60, 'ע': 70, 'פ': 80, 'ף': 800, 'צ': 90, 'ץ': 900, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    
    # Obtener el valor numérico de la letra
    valor = gematría_hebrea.get(letra, 0)
    return valor

def obtener_gematría_palabra(palabra):
    # Calcular la gematría total de la palabra
    suma = sum(calcular_gematría(letra) for letra in palabra)
    return suma

def obtener_significados(letras):
    # Diccionario de correspondencia entre letras y sus significados
    significados = {
        'א': 'Principio, Creación',
        'ב': 'Unión, Construcción',
        'ג': 'Fuerza, Conexión',
        'ד': 'Puerta, Conocimiento',
        'ה': 'Revelación, Existencia',
        'ו': 'Vida, Unidad',
        'ז': 'Corazón, Reflexión',
        'ח': 'Vida, Éxito',
        'ט': 'Energía, Bondad',
        'י': 'Creación, Manifestación',
        'כ': 'Poder, Potencial',
        'ל': 'Elevación, Instrucción',
        'מ': 'Unión, Completitud',
        'נ': 'Transformación, Continuidad',
        'ס': 'Protección, Ocultamiento',
        'ע': 'Sabiduría, Visión',
        'פ': 'Boca, Expresión',
        'צ': 'Justicia, Equilibrio',
        'ק': 'Santa, Vinculación',
        'ר': 'Cabeza, Liderazgo',
        'ש': 'Fuego, Espíritu',
        'ת': 'Verdad, Perfección',
        'ך': 'Poder, Potencial',
        'ם': 'Unión, Completitud',
        'ן': 'Transformación, Continuidad',
        'ף': 'Boca, Expresión',
        'ץ': 'Justicia, Equilibrio'
    }
    
    # Obtener los significados de las letras ingresadas
    significado1 = significados.get(letras[0], "Sin significado conocido")
    significado2 = significados.get(letras[1], "Sin significado conocido")
    significado3 = significados.get(letras[2], "Sin significado conocido")
    
    return significado1, significado2, significado3

def obtener_palabra(letras):
    # Diccionario de correspondencia entre letras y palabras en hebreo
    palabras = {
        'א': 'Aleph',
        'ב': 'Bet',
        'ג': 'Gimel',
        'ד': 'Dalet',
        'ה': 'Hei',
        'ו': 'Vav',
        'ז': 'Zayin',
        'ח': 'Chet',
        'ט': 'Tet',
        'י': 'Yod',
        'כ': 'Kaf',
        'ל': 'Lamed',
        'מ': 'Mem',
        'נ': 'Nun',
        'ס': 'Samech',
        'ע': 'Ayin',
        'פ': 'Pei',
        'צ': 'Tzadi',
        'ק': 'Kuf',
        'ר': 'Reish',
        'ש': 'Shin',
        'ת': 'Tav',
        'ך': 'Kaf (final)',
        'ם': 'Mem (final)',
        'ן': 'Nun (final)',
        'ף': 'Pei (final)',
        'ץ': 'Tzadi (final)'
    }
    
    # Obtener la palabra formada por las letras ingresadas
    palabra1 = palabras.get(letras[0], "Desconocida")
    palabra2 = palabras.get(letras[1], "Desconocida")
    palabra3 = palabras.get(letras[2], "Desconocida")
    
    return palabra1, palabra2, palabra3

def significado_gematría(suma):
    # Diccionario de significados de gematría
    significados = {
        1: 'Unidad, Principio',
        2: 'Dualidad, Separación',
        3: 'Trinidad, Unión',
        4: 'Creación, Mundo Material',
        5: 'Gracia, Favor',
        6: 'Poder, Creación',
        7: 'Perfección, Compleción',
        8: 'Nuevo Comienzo, Renacimiento',
        9: 'Finalización, Plenitud',
        10: 'Perfección, Totalidad',
        20: 'Poder, Potencial',
        30: 'Elevación, Instrucción',
        40: 'Unión, Completitud',
        50: 'Cincuenta, Espíritu Santo',
        60: 'Protección, Ocultamiento',
        70: 'Sabiduría, Visión',
        80: 'Boca, Expresión',
        90: 'Justicia, Equilibrio',
        100: 'Santa, Vinculación',
        200: 'Cabeza, Liderazgo',
        300: 'Fuego, Espíritu',
        400: 'Verdad, Perfección',
        500: 'Kaf (final)',
        600: 'Mem (final)',
        700: 'Nun (final)',
        800: 'Pei (final)',
        900: 'Tzadi (final)'
    }
    
    if suma in significados:
        return significados[suma]
    else:
        return "Sin significado conocido para esta gematría"

# Entrada de usuario
letra1 = input("Ingrese la primera letra hebrea (1-22): ")
letra2 = input("Ingrese la segunda letra hebrea (1-22): ")
letra3 = input("Ingrese la tercera letra hebrea (1-22): ")

# Calcular la suma de gematría
suma = calcular_gematría(letra1) + calcular_gematría(letra2) + calcular_gematría(letra3)

# Obtener los significados de las letras
significado1, significado2, significado3 = obtener_significados([letra1, letra2, letra3])

# Obtener la palabra formada por las letras ingresadas
palabra1, palabra2, palabra3 = obtener_palabra([letra1, letra2, letra3])

# Obtener el significado de la gematría
significado_gematría = significado_gematría(suma)

# Imprimir resultados
print("La suma de gematría es:", suma)
print("Significado de", letra1 + ":", significado1)
print("Significado de", letra2 + ":", significado2)
print("Significado de", letra3 + ":", significado3)
print("Palabra formada por las letras ingresadas:", palabra1, palabra2, palabra3)
print("El significado de la gematría", suma, "es:", significado_gematría)
