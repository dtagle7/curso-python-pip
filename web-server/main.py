import store
from fastapi import FastAPI # Importando FastAPI
from fastapi.responses import HTMLResponse # Se importa HTML response para poder crear paginas html

app = FastAPI() # Creando una instancia de FastAPI

@app.get('/') # decorador, se especifica la ruta por la cual desde la web se va a poder a ingresar 
def get_list():
    return [1 , 2 , 3]

@app.get('/contact' , response_class=HTMLResponse) # Se tiene que añadir el argumento response_class=HTMLResponse para poder retornar html
def get_list():
    # Dentro del return se coloca el codigo html que se desea retornar entre tripe doble comilla
    return """ 
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()

