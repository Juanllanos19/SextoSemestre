def verificar_prueba(cadena):
    datos = cadena.split(",")
    
    if not (2 <= len(datos[0]) <= 12 and datos[0].isalpha()):
        return "El nombre del producto debe ser de un largo entre 2 y 12 caracteres y solo contener letras."
    
    numeros = []
    for elem in datos[1:]:
        if elem.strip().isdigit():
            num = int(elem.strip())
            if 1 <= num <= 48:
                numeros.append(num)
            else:
                return f"El tamaño {num} está fuera del rango permitido."
    
    if numeros != sorted(numeros):
        return "Los tamaños no están en orden ascendente."
    
    
    return "El producto ha sido registrado con exito"

def test_verificar_entrada():
    assert verificar_prueba("cocacola,1,2,3,4,5") == "El producto ha sido registrado con exito"
    assert verificar_prueba("Squirt,1,2,3") == "El producto ha sido registrado con exito"
    assert verificar_prueba("abc,1,2,3,49") == "El tamaño 49 está fuera del rango permitido."
    assert verificar_prueba("abc,1,2,0") == "El tamaño 0 está fuera del rango permitido."
    assert verificar_prueba("Sprite,1,2,3,4,5") == "El producto ha sido registrado con exito"
    assert verificar_prueba("abc,1,2,3,4,5,49") == "El tamaño 49 está fuera del rango permitido."
    assert verificar_prueba("abc,1,2,3,4,0") == "El tamaño 0 está fuera del rango permitido."
    assert verificar_prueba("1234,1,2,3") == "El nombre del producto debe ser de un largo entre 2 y 12 caracteres y solo contener letras."
    assert verificar_prueba("pepsi,1,2,3,5,4") == "Los tamaños no están en orden ascendente."
    assert verificar_prueba("fanta,1,2,3,5,6") == "El producto ha sido registrado con exito"

test_verificar_entrada()
