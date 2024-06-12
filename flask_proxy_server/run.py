import sys
sys.path.append('app')
sys.path.append('app/routes')

from run_helper import app

from app.routes.food_classification.tomato_classification_blueprint import tomato_classification_blueprint

app.register_blueprint(tomato_classification_blueprint)

if __name__ == '__main__':
    app.run(threaded=True)