import unittest
import wc

class Testwc(unittest.TestCase):
    maxDiff = None
    def test_existe_wc(self):
        w = wc.Wc()
        self.assertIsNotNone(w)

    def test_validar_archivo_texto_es_correcto(self):
        w = wc.Wc('/home/teo/proyectos/wc/uno.html')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp, True)

    def test_validar_archivo_texto_es_incorrecto(self):
        w = wc.Wc('/home/teo/proyectos/wc/bolas_chicle.jpg')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp, False)        

    def test_validar_archivo_inexistente_es_incorrecto(self):
        w = wc.Wc('/home/teo/proyectos/wc/bolas_chicle.jpg')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp, False)  

    def test_abrir_archivo_correcto(self):
        html = """Hola\ncaracola sdlkrg ñsldkj m"""
        w = wc.Wc('/home/teo/proyectos/wc/uno.html')
        w.abrir_archivo()
        self.assertEqual(w._Wc__contenido,html )
    
    def test_abrir_archivo_inexistente_da_error(self):
        w = wc.Wc('/home/teo/ggg')
        with self.assertRaises(Exception):
            resp = w.abrir_archivo()
              
    def test_contar_lineas_correcto(self):
        html = """Hola\ncaracola sdlkrg ñsldkj m"""
        w = wc.Wc('/home/teo/proyectos/wc/uno.html')
        w.abrir_archivo()
        w.contar_lineas()
        self.assertEqual(w._Wc__cnt_lineas,3)

    def test_cadena_a_texto_limpio(self):
        w = wc.Wc('/home/teo/proyectos/wc/uno.html')
        txt = """hola\ncaracola sdlkrg ñsldkj m\nen"""
        w.abrir_archivo()
        resp = w._Wc__limpiar_cadena()
        self.assertEqual(w._Wc__contenido, txt)