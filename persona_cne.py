
import requests
from bs4 import BeautifulSoup


class persona():
    def __init__(self):
        self.nationality = ''
        self.id = ''
        self.__full_name = ''
        self.__state = ''
        self.__municipality = ''
        self.__parish = ''
        self.status = False

############################################################
#   Metodos para acceder a los atributos del objeto persona
############################################################

    def get_nationalidad(self):# Nacionalidad V:Venezolano / E:Extranjero
        return self.nationality.capitalize()

    def get_id(self):# Número de identificación ciudadana (Cédula)
        return self.id

    def get_full_name(self):# Nombre completo de la persona
        return self.__full_name

    def get_state(self):# Estado donde se encuentra registrado para ejercer el voto
        return self.__state

    def get_municipality(self):# Municipio donde se encuentra registrado para ejercer el voto
        return self.__municipality

    def get_parish(self):# Parroquia donde se encuentra registrado para ejercer el voto
        return self.__parish

    def get_status(self):
        return self.status
#################################################################################################
#   consulta(self, id_nacionalidad, id_cedula) realiza un requests a cne.gob.ve para raspar los
#   datos correspondientes.
#################################################################################################

    def consulta(self, id_nacionalidad, id_cedula):
        # Construye la url objetivo para el raspado de los datos
        url = "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=" + id_nacionalidad.capitalize() \
              + "&cedula=" + id_cedula

        global requests

        response = requests.get(url)

        # Parseamos el HTML
        soup = BeautifulSoup(response.content, "html.parser")

        if response.status_code == 200:

            # Llama a __validar(self, argumento) para validar el contenido del <td> 19 del árbol HTML
            if self.__validar(self, soup.find_all('td')[19].text):
                print(id_nacionalidad.capitalize() + '-' + id_cedula + '|','REGISTRO INEXISTENTE')

            else:
                if (soup.find_all('td')[8].text.strip() == 'DATOS PERSONALES'):
                    print(id_nacionalidad.capitalize() + '-' + id_cedula + '|', 'REGISTRO CON OBJECIÓN')
                else:
                    # soup.find busca entre las etiquetas de la estructura HTML
                    self.__full_name = soup.find_all('td')[13].text
                    self.__state = soup.find_all('td')[15].text
                    self.__municipality = soup.find_all('td')[17].text
                    self.__parish = soup.find_all('td')[19].text
                    self.status = True
        else:
            print("Error de conexión: Codigo ", response.status_code)
            self.consulta(self, id_nacionalidad, id_cedula)

    @staticmethod
    def __validar(self, argumento):
        if argumento == "Objeción: FALLECIDO (3)" or argumento == "RECOMENDACIONES" or argumento == "\x08":
            return True
        else:
            return False
