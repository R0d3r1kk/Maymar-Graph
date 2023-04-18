from api import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    type = db.Column(db.Integer)
    date_created = db.Column(
        "date_created", db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    date_updated = db.Column(
        "date_updated", db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    
    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "type": self.type,
            "date_created": self.date_created,
            "date_updated": self.date_updated,
        }

    def __repr__(self):
        return "<User: %r %r %r>" % (self.name, self.firstname, self.lastname)


class CUserType(db.Model):
    __tablename__ = "CUserType"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20))
    idpermission = db.Column(db.Integer)

    def __init__(self, role=None, idp=None):
        self.role = role
        self.idpermission = idp

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "role": self.role,
            "idpermission": self.idpermission,
        }

    def __repr__(self):
        return f"<role={self.role}, permission={self.idpermission}>"
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CTableType(db.Model):
    __tablename__ = "CTableType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name=None):
        self.vame = name

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self):
        return f"<name={self.name}>"
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class CLocation(db.Model):
    __tablename__ = "CLocation"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name=None):
        self.vame = name

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self):
        return f"<name={self.name}>"
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
