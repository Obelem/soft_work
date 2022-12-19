from web import app
from os import getenv

if __name__ == "__main__":
    port = getenv('PORT')
    port = '5000' if port is None else port

    app.run(debug=True, port=port)
