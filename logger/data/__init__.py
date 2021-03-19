from flask_sqlalchemy import SQLAlchemy
from business import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/logger.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)