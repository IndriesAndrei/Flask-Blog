# we will import app from flaskblog folder and the __init__.py file
from flaskblog import app

# we run the app in Debug mode, so not to have to restart server every time
if __name__ == '__main__':
    app.run(debug=True)

