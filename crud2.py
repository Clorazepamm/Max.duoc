import csv
# Crear, leer, actualizar y eliminar

def abrir_csv():
    with open('people_list.csv',mode= 'r', encoding= 'utf-8', newline='') as archivos_csv:
        datoscsv = csv.DictReader(archivos_csv)
        return(list(datoscsv))

def leer_csv():
    datos = abrir_csv()
    
    for linea in datos:
        print(linea)     

def crear_persona_csv():
    datos = abrir_csv()
    
    nueva_persona = {'DNI':input('ingrese una dni: '),
                    'Nombre':input('ingrese un nombre: '),
                    'Edad':input('ingrese una edad: ')
                    } 
    
    datos.append(nueva_persona)
    with open('people_list.csv', mode='w', encoding= 'utf-8',  newline='') as archivos_csv:
        datos_escribir = csv.DictWriter(archivos_csv,fieldnames=['DNI','Nombre','Edad'])
        datos_escribir.writeheader()
        datos_escribir.writerows(datos)
        
def editar_personas():
    datos = abrir_csv()
    buscar_dni = input('ingrese un dni')

    for linea in datos:
        if linea['DNI'] == buscar_dni:
            print(linea)
            editador_persona = {'Nombre':input('ingrese un nombre: '),
                    'Edad':input('ingrese una edad: ')
                    }
            linea.update(editador_persona)
    
    with open('people_list.csv', mode='w', encoding= 'utf-8',  newline='') as archivos_csv:
        datos_escribir = csv.DictWriter(archivos_csv,fieldnames=['DNI','Nombre','Edad'])
        datos_escribir.writeheader()
        datos_escribir.writerows(datos)

def eliminar_persona():
    datos = abrir_csv()
    buscar_dni = input('ingrese una dni a eliminar: ')
    
    for posicion,linea in enumerate(datos):
        if linea['DNI'] == buscar_dni:
            print(linea)
            del datos[posicion]
       
    with open('people_list.csv', mode='w', encoding= 'utf-8',  newline='') as archivos_csv:
        datos_escribir = csv.DictWriter(archivos_csv,fieldnames=['DNI','Nombre','Edad'])
        datos_escribir.writeheader()
        datos_escribir.writerows(datos)        

datos_csv = abrir_csv
#eliminar_persona()
#editar_personas()
#crear_persona_csv()
#leer_csv()
""" print(abrir_csv()) """

while True:
    print('******menu*****')
    print('[1] crear')
    print('[2] eliminar')
    print('[3] editar')
    print('[4] leer')
    print('[0] salir ')
    opcion = int(input('ingrese una opcion: '))

    if opcion == 1:
        crear_persona_csv()
    if opcion ==2:
        eliminar_persona()
    if opcion == 3:
        editar_personas()
    if opcion == 4:
        leer_csv()
    elif opcion == 0:
        break