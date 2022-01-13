#from _typeshed import WriteableBuffer
import persona_cne as cne
import csv
import os



limpiaPantalla = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def wait(): 
    char = input('')


if __name__ == '__main__':
    listado = []
        
    limpiaPantalla()
    print('***************************************************************\n')
    print('****    Nombre del archivo precargado: origen.csv          ****\n')
    print('**** Si presiona enter éste se cargará automáticamente     ****\n')  
    print('**** SI desea cargarr su propio archivo ingrese nombre:    ****\n')
    print('**** Hay una salida por pantalla y el archivo csv generado ****\n')
    print('****     El archivo se llama: listado_CNE.csv              ****\n')
    print('****     Presione tecla ENTER para continuar               ****\n')
    print('***************************************************************\n')
    wait()
    limpiaPantalla()
    print('*******************************************************************\n')
    print ('*****              Ingrese el Nombre del archivo             *****\n')
    print('******   Si presiona enter éste se cargará automáticamente     ****\n') 
    print('*******************************************************************\n')
    archivo = input(' ') or 'origen.csv'
    #limpiaPantalla()
    print('Estableciendo la conexión...')
    
    # Apertura del archivo
    with open(archivo, newline='', encoding='utf8') as csvfile_entrada:
        reader = csv.DictReader(csvfile_entrada, delimiter=',')  # Create object reader of DirectReader type
        
        
        limpiaPantalla()
        # Se recorre las filas del archivo.csv
        with open('listado_CNE.csv', 'w') as csvfile:
                    fieldnames = ['cedula', 'nombre', 'estado', 'municipio', 'parroquia' ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,  delimiter = '|')
                    #writer.writeheader()
                    for row in reader:
                        persona = cne.persona()  # Create object  persona type
                        # Asociación de las variables con los titulos de las columnas
                        nacionalidad = row['nacionalidad']
                        cedula = row['cedula']

                        persona.consulta(nacionalidad, cedula)
                        if persona.status:
                            print(nacionalidad.capitalize() + '-' + cedula + "|" + persona.get_full_name() + "|" + persona.get_state() + "|" +
                                persona.get_municipality() + "|" + persona.get_parish())
                            cedula = nacionalidad.capitalize() + '-' + cedula
                            nombre = persona.get_full_name()
                            estado = persona.get_state()
                            municipio = persona.get_municipality()
                            parroquia = persona.get_parish()


                            listado = [{ 'cedula' : cedula,'nombre' : nombre , 'estado' : estado, 'municipio' : municipio, 'parroquia' : parroquia},]
                            writer.writerows(listado)
                            
                        else:
                            pass

                        del persona
                    
        #csvfile.close()
        del csvfile
    #csvfile_entrada.close()
    del csvfile_entrada
                    