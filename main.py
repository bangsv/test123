from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для корневого URL "/"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Запускаем сервер Flask
if __name__ == '__main__':
    app.run()
