import flask from Flask
from flask_smorest import Api

app = Flask(__name__)

kitchen_api = Api(app)