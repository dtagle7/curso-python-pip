import requests # importando la libreria instalada requests que permite hacr peticiones a otro tipo de servidores web desde Pyhton

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # conectandonos a una API
    print(r.status_code) # cuando consumes una API tienes un estado, esto es lo que estamos imprimiendo
    print(r.text)
    print(type(r.text))
    categories = r.json() # con el metodo json podemos transformar la variable r.text en una lista para poder iterarla. Por defecto esta variable es string
    for category in categories: # categories es una lista de diccionarios
        print(category['name'])
    