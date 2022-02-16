# import mimetypes

# c=open('/home/teo/proyectos/wc/README.md')
# mime = mimetypes.guess_type('/home/teo/proyectos/wc/project1.ico')
# print(mime)

class Wc():
    def __init__(self) -> None:
        self.__cnt_palabras = 0
        self.__cnt_lineas = 0
        self.__ocurrencias = {}
    
    @property
    def numero_palabras(self):
        pass
    

        