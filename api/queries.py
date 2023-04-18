
from .models import User, CUserType, CTableType, CLocation, db

# Returns all the users from the database.
def get_users_resolver(obj, info):
	try:
		cols = [
            "id",
            "name",
            "firstname",
            "lastname",
            "email",
	    	"password",
            "phone",
            "type",
            "date_created",
            "date_updated",
        ]
		# Grabs all the users and puts them into a list of dictionaries.
		users = [{col: getattr(d, col) for col in cols} for d in User.query.all()]
		print(users)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"users": users
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
		
	return payload

def get_users_types_resolver(obj, info):
	try:
		cols = [
            "id",
            "role",
            "idpermission",
        ]
		# Grabs all the users and puts them into a list of dictionaries.
		types = [{col: getattr(d, col) for col in cols} for d in CUserType.query.all()]
		print(types)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"types": types
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_table_types_resolver(obj, info):
	try:
		cols = [
            "id",
            "name",
        ]
		# Grabs all the users and puts them into a list of dictionaries.
		types = [{col: getattr(d, col) for col in cols} for d in CTableType.query.all()]
		print(types)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"types": types
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_zones_resolver(obj, info):
	try:
		cols = [
            "id",
            "name",
        ]
		# Grabs all the users and puts them into a list of dictionaries.
		zones = [{col: getattr(d, col) for col in cols} for d in CLocation.query.all()]
		print(zones)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"zones": zones
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_user_resolver(obj, info, id):
	try:
		user = User.query.get(id)
		payload = {
			"success": True,
			"user": user.serialize
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload