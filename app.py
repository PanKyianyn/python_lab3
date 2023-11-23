# создаем екземпляр класса flask
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#запускаем сервер разработки flask c значениями узла и порта
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

#назначаем функцию маршруту URL адресов
@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


