from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app import login_manager

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    _password = Column(String, nullable=True)
    authenticated = Column(Boolean, default=False)
    registered_on = Column(DateTime, nullable=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password).decode("utf-8")

    @hybrid_method
    def is_correct_password(self, password):
        if self.password is not None:
            return bcrypt.check_password_hash(self.password, password)
        else:
            return None

    @hybrid_property
    def name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    def get_id(self):
        """Return the id"""
        return str(self.id)

    def __repr__(self):
        return '<User: {}>'.format(self.email)
