from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:flask@db:3306/flask_16"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sadasdsdssadsadsadsadsadssaddas"
db.init_app(app)


with app.app_context():
    from routes import *
    from models import User

    migrate = Migrate(app, db)


from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_restful import Resource


api = Api(app)

@app.route("/api/spec")
def spec():
    return swagger(app)


class MyResource(Resource):
    @swagger.operation(
        notes='Get a list of items',
        parameters=[
            {
                "name": "page",
                "description": "Page number",
                "required": False,
                "type": "int",
                "paramType": "query"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Success"
            },
            {
                "code": 400,
                "message": "Invalid input"
            }
        ]
    )
    def get(self):
        # Code to get items
        return {'items': items}

api.add_resource(MyResource, '/items')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
