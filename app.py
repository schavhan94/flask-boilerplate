from . import *
from .home.views import home_blueprint

app.register_blueprint(home_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)