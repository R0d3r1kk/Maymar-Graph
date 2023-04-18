from .models import User, db
from ariadne import convert_kwargs_to_snake_case
from sqlalchemy.sql import text

@convert_kwargs_to_snake_case
def create_user_resolver(obj, info, name,
    firstname,
    lastname,
    email,
    password,
    phone,
    type):
    try:
        cursor = db.engine.raw_connection().cursor()
        params =[name, firstname, lastname, email, password, phone, type]
        cursor.execute("create_user ?, ?, ?, ?, ?, ?, ?", params)
        cursor.commit()
        user = User.query.filter_by(email=email).first()
        payload = {
            "success": True,
            "user": user
        }    
    except Exception as error:
		# Create a payload that contains the thrown exception.
        payload = {
			"success": False,
			"errors": [str(error)]
		}
    return payload
