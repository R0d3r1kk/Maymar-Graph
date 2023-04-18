
from .models import User, CUserType, CTableType, CLocation, Table, Reservation, db

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

def get_table_resolver(obj, info, id):
	try:
		cursor = db.engine.raw_connection().cursor()
		table = cursor.execute("get_table ?", [id]).fetchone()
		cursor.commit()
		print(table)
		payload = {
			"success": True,
			"table": table
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_tables_resolver(obj, info):
	try:
		cols = [
            "id",
            "capacity",
	    	"table_zone",
		    "table_type",
		    "table_status"
        ]
		
		cursor = db.engine.raw_connection().cursor()
		res = cursor.execute("get_tables ", []).fetchall()
		cursor.commit()
		# Grabs all the users and puts them into a list of dictionaries.
		tables = [{col: getattr(d, col) for col in cols} for d in res]
		print(tables)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"tables": tables
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_reservation_resolver(obj, info, id):
	try:
		cursor = db.engine.raw_connection().cursor()
		res = cursor.execute("get_reservation ?", [id]).fetchone()
		cursor.commit()
		print(res)
		payload = {
			"success": True,
			"reservation": res
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload

def get_reservations_resolver(obj, info):
	try:
		cols = [
          	"reservation_id",
			"reservation_date",
			"user_id",
			"user_fullname",
			"user_email",
			"user_phone",
			"table_id",
			"table_capacity",
			"table_zone",
			"table_type",
			"table_status",
			"reservation_created",
			"reservation_updated",
        ]
		
		cursor = db.engine.raw_connection().cursor()
		res = cursor.execute("get_reservations ", []).fetchall()
		cursor.commit()
		# Grabs all the users and puts them into a list of dictionaries.
		res = [{col: getattr(d, col) for col in cols} for d in res]
		print(res)
		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"reservations": res
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload