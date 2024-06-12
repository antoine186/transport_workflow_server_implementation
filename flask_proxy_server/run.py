import sys
sys.path.append('app')
sys.path.append('app/routes')

from run_helper import app

from app.routes.request_transport_blueprint import request_transport_blueprint

app.register_blueprint(request_transport_blueprint)

if __name__ == '__main__':
    app.run(threaded=True)