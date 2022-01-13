# bloomckerRPA
Desarrollador RPA en Bloomcker


Hay dos (2) planteamientos en el repositorio:

El primero, denominado "consulta_cne.py", tiene dos opciones: 
 1.- leer un archivo denominado "origen.csv" que contiene dos columnas: nacionalidad y cedula, o 
 2.- permite el ingreso por consola del nombre de una archivo tipo "nombre_archivo.csv" (el cual también debe contener dos columnas: nacionalidad y cedula)  
 y haciendo uso de la clase persona_cne.py presenta el listado por consola del nombre completo de la(s) persona(s), estado(s), municipio(s) y parroquia(s). 
 Luego se hace un volcado de la data en un archivo con formato csv denominado "listado_CNE.csv". Este archivo tiene los valores de las columnas Cédula, Nombre, 
 Estado, Municipio y Parroquia
Nota: El programa permite que con solo presionar "Enter" se cargue automáticamente el archivo de la primera opción. Fuente consultada: @oswaldom_code

El segundo, denominado "covid_API.py", consulta los datos de la API : https://covid19-api.com/docs. Obtiene y muestra por pantalla los valores de todos los países con las categorías País, Confirmados, Recuperados, Críticos y Fallecidos. Luego genera un archivo denominado "listado_COVID19.csv" que  contiene las mismas categorías antes mencionadasd.

NOTA: El segundo planteamiento hace uso de pandas para generar el archivo "listado_COVID19.csv"
