"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
# Nuevo valor por defecto para el orden
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    # La función sorted usa reverse=True para orden descendente
    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    # Inicializa el nuevo parámetro de orden
    is_ascending = DEFAULT_ASCENDING
    
    # -----------------------------------------------------------
    # Ahora esperamos 3 argumentos: [filename] [remove_duplicates] [order]
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        # El tercer argumento ('asc' o 'desc') determina el orden
        is_ascending = sys.argv[3].lower() == "asc"
    else:
        print("Argumentos requeridos no proporcionados.")
        print("Uso: python main.py <nombre_fichero> <eliminar_duplicados ('yes'/'no')> <orden ('asc'/'desc')>")
        sys.exit(1)
    # -----------------------------------------------------------

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    word_list.append(line.strip())
        except Exception as e:
            print(f"Error al leer el fichero: {e}")
            sys.exit(1)
    else:
        print(f"El fichero {filename} no existe. Usando lista por defecto.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Llama a sort_list con el nuevo parámetro de orden
    print(sort_list(word_list, is_ascending))