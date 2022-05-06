import random


def resolver_problema(iteraciones, new_list):
    if new_list == 0:
        with open('keylog.txt', 'r') as f:
            algo = f.read()
        lista_secuencias = algo.splitlines()
    else:
        lista_secuencias = new_list
        lista_secuencias = [str(x) for x in lista_secuencias]
    # Se inicializa con el valor del numero de combinaciones maximas
    lon_clave = len(lista_secuencias[0]) * 10
    for i in range(iteraciones):
        random.shuffle(lista_secuencias)
        construccion_clave = str('')
        # Itera en x cada una de las secuencias
        for x in lista_secuencias:
            # idx_previous guarda la posicion del digito anterior de la misma secuencia
            idx_previous = -1
            # Itera en y cada uno de los valores de la secuencia x
            for id_y in range(len(str(x))):
                # Define parte del vector en el que puede aomodarse el numero y siendo id_y la posicion dentro de la secuencia
                cadena_en_revision = [x for x in range(idx_previous + 1, len(construccion_clave))]
                y = str(x)[id_y]
                inserted_value = False
                cadena_rev_real = {
                    x: str(construccion_clave[x]) for x in cadena_en_revision if x >= 0
                }
                # Revisa si el valor ya esta en clave, y si esta solo actualiza el indice de busqueda
                if str(y) in cadena_rev_real.values():
                    idx_previous = int([x for x in cadena_rev_real if cadena_rev_real[x] == str(y)][0])
                else:
                    # Si no esta el valor busca el mejor lugar para ingresarlo
                    for z in cadena_en_revision:
                        if int(y) < int(construccion_clave[z]):
                            construccion_clave = construccion_clave[:z] + str(y) + construccion_clave[z:]
                            idx_previous = z + 1
                            inserted_value = True
                            break
                    # Si no lo pudo ingresar lo ingresa al final
                    if not inserted_value:
                        construccion_clave += str(y)
                        idx_previous = len(construccion_clave)

        if len(construccion_clave) < lon_clave:
            lon_clave = len(construccion_clave)
            clave = construccion_clave

    return clave
