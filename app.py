from flask import Flask
from Views.home import url_view
from flask_script import Manager

app = Flask(__name__)
app.register_blueprint(blueprint=url_view)
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()
