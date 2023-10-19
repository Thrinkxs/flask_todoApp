# from flask import Flask, render_template, request, redirect, url_for
# from routes import blueprint
# # from config import db

# # initialize app
# app = Flask(__name__, template_folder='../frontend/templates',
#             static_folder='../frontend/static')

# # register route blueprint
# app.register_blueprint(blueprint)

# # with app.app_context():
# #     db.create_all()

# if __name__ == "__main__":
#     app.run(debug=True)
from app import create_app, db


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
