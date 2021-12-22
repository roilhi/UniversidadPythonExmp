def listarTerminos(nombre, *nombres,**terminos):
    """Recibe argumentos llave valor (diccionario o kwargs)
    nombre = argumento fijo
    *nombres = argumentos lista variables (tupla)
    **terminos= argumentos llave-valor (diccionario) """
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Environment',PK='Primary Key')
listarTerminos(DBMS='Database Management System')
