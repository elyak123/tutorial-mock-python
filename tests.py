import json
import unittest
from unittest import mock
from ejemplo import main
from ejemplo_side_effect import main as side_main


@mock.patch('ejemplo.time.sleep')
@mock.patch('ejemplo.print')
class MainTest(unittest.TestCase):

    def test_do_sleep(self, mock_print, mock_sleep):
        """
        1.- Descripción de la prueba (test)
        * Al inicio de la función main, se ejecuta un time sleep por
          15 segundos.
        2.- Requerimientos del entorno (setting)
        * Hacer un mock de ejemplo.print para mantener limpio el stdout
        * Hacer un mock de ejemplo.time.sleep
        3.- Inferencias con resultados conocidos
        * No son necesarias para esta prueba
        4.- Evaluación / Assertions
        * Verificar que ejemplo.time.sleep fue ejecutado con 15 como argumento
        * Asegurar que ejemplo.print se ejecutó con 'Soy Unix!!' como argumento
        """
        main()
        mock_sleep.assert_called_with(15)
        mock_print.assert_called_with('Soy Unix!!')

    @mock.patch('ejemplo.sys.platform', 'win32')
    def test_platform_windows(self, mock_print, mock_sleep):
        """
        1.- Descripción de la prueba (test)
        * main deberá imprimir Soy Windows!!
        requerimientos.
        2.- Requerimientos del entorno (setting)
        * Hacer un mock de ejemplo.print para evitar ensuciar el stdout
        * Hacer un mock de ejemplo.time.sleep para agilizar la prueba.
        3.- Inferencias con resultados conocidos.
        * sys.platform deberá regresar 'win32'
        4.- Evaluacion / Assertions
        * Comprobar que ejemplo.print fue llamado con el string:
          Soy Windows!!
        """
        main()
        mock_print.assert_called_with('Soy Windows!!')

    @mock.patch('ejemplo.sys.platform', 'cygwin')
    def test_platform_windows_cygwin(self, mock_print, mock_sleep):
        """
        1.- Descripción de la prueba (test)
        * main deberá imprimir Soy Windows!!
        2.- Requerimientos del entorno (setting)
        * Hacer un mock de ejemplo.print para evitar ensuciar el stdout
        * Hacer un mock de ejemplo.time.sleep para agilizar la prueba.
        3.- Inferencias con resultados conocidos
        * sys.platform deberá regresar 'cygwin'
        4.- Evaluación / Assertions
        * Comprobar que ejemplo.print fue llamado con el string:
          Soy Windows!!
        """
        main()
        mock_print.assert_called_with('Soy Windows!!')


@mock.patch('ejemplo_side_effect.print')
@mock.patch('ejemplo_side_effect.requests.get')
class SideMainTest(unittest.TestCase):

    def test_main_raises_runtimeerror(self, mock_get, mock_print):
        """
        1.- Descripción de la prueba (test)
        2.- Requerimientos del entorno (setting)
        3.- Inferencias con resultados conocidos
        4.- Evaluación / Assertions
        """
        mock_get.side_effect = RuntimeError
        with self.assertRaises(RuntimeError):
            side_main()
        mock_get.assert_called_with('http://localhost/fake-url/')
        mock_print.assert_called_with('This was a mistake')

    def test_main_returns_200(self, mock_get, mock_print):
        """
        1.- Descripción de la prueba (test)
        2.- Requerimientos del entorno (setting)
        3.- Inferencias con resultados conocidos
        4.- Evaluación / Assertions
        """
        attrs = {'json.return_value': json.dumps({'hola': 'foo bar'})}
        mock_response = mock.MagicMock()
        mock_response.configure_mock(**attrs)
        mock_get.return_value = mock_response
        side_main()
        mock_print.assert_called_with(json.dumps({'hola': 'foo bar'}))


if __name__ == '__main__':
    unittest.main()
