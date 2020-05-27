# Tutorial de mock en python
Tutorial de unittest.mock para reunion de Python Tijuana.

La idea principal es hacer ejercicios con funcionalidad mínima pero que permitan mostrar funcionalidades de esta librería estándar de python.

# Dependencias

Solo tiene necesitas hacer:

`pip install -r requirements.txt`

# Ejecución
Para ejecutar las pruebas simplemente es necesario:

`python tests.py`

# Que son estos docstrings que tiene cada test?

Con el tiempo he observado que para realizar mocks es muy importante no soltar la vista de lo que realmente estamos probando, es decir, que sin algo que nos recuerde el objetivo del test podemos realizar `Mock`s fuera del alcance de nuestro test, causando falsos positivos.

Por lo que los docstrings en cada test son nuestra guia:
1. Descripción de la prueba (test)
2. Requerimientos del entorno (setting)
3. Inferencias con resultados conocidos
4. Evaluación / Assertions

Espero que les sirva :)
