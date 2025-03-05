def es_palindromo(cadena):
    """Devuelve si es una cadena de texto es palíndromo o no

    Args:
        cadena (str): Cadena de texto 

    Returns:
        bool: Devuelve si es verdadero o falso que la cadena de texto es palíndromo
    """
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola mundo"))"# Nueva actualizaci�n" 
