from src.app import app
from src.controllers import *


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=302,
        debug=True
    )