def ClasificaGenero(dataset, _len=100):

    """
    Realizado Alvaro Morales
    
    Función que calcula el % de hombres y mujeres

    El dataset debe ser una lista que contiene "F" para mujeres y "M" para hombres (de tamaño 100 por defecto)

    Devuelve False si el dato no es correcto (e imprime el motivo)

    """

    # Check Type

    if type(dataset) != list:

        print("Dataset is not a list")

        return False



    # Check Len

    if len(dataset) != _len:

        print("Wrong dataset size (must be) 100")

        return False



    uniq_values = set(dataset)

    if uniq_values != {"F", "M"}:

        print("Values must")

        return False



    n_hombres = len([gender for gender in dataset if gender == "M"])

    p_hombres = n_hombres / _len * 100

    p_mujeres = 100 - p_hombres

    print(f"Hay {p_hombres}% de hombres y {p_mujeres}% mujeres")

    if p_hombres > 50:

        print("Hay más hombres")

    elif p_hombres < 50:

        print("Hay más mujeres")

    else:

        print("Hay igualdad")

    return True