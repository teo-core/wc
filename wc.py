import mimetypes

class Wc():
    def __init__(self,archivo='') -> None:
        self.__archivo = archivo
        self.__cnt_palabras = 0
        self.__cnt_lineas = 0
        self.__ocurrencias = {}
        self.__contenido = ''
    
    @property
    def numero_palabras(self):
        return self.__cnt_palabras
    

    def __validar_archivo(self):
        mime = mimetypes.guess_type(self.__archivo)
        try:
            resp = mime[0].split('/')[0] == 'text'
            return resp
        except AttributeError:
            raise Exception('Archivo inexistente o inválido')


    def abrir_archivo(self):
        try:
            if self.__validar_archivo():
                with open(self.__archivo,'r') as manejador:
                    texto = manejador.read()
                    if texto != '':
                        self.__contenido = texto
        except Exception as e:
            raise e

    def contar_lineas(self):
        self.__cnt_lineas = len(self.__contenido.split('\n'))

    


        