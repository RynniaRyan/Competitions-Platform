from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from sqlalchemy import Enum
import datetime

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    profile_picture = db.Column(db.String(255), nullable=False) #default='default_profile_picture.jpg'
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    date_joined = db.Column(db.DateTime)

    role = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': role,
    }

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.role = role
        self.date_joined = datetime.utcnow()
        self.set_password(password)
        

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'profile_picture': self.profile_picture,
            'date_joined': self.date_joined
        }
    
    def __repr__(self):
        return (f"<Username: {self.username} | "
                f"Email: {self.email} | "
                f"Role: {self.role} | "
                f"Date Joined: {self.date_joined}>")

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)