from App.database import db
from App.models import User

class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def __init__(self, username, email, password, firstname, lastname, role='admin'):
        super().__init__(username, email, password, role)
        self.firstname = firstname
        self.lastname = lastname
    
    def get_json(self):
        json_data = super().get_json()
        json_data.update({
            'firstname' : self.firstname,
            'lastname' : self.lastname
        })
        return json_data
    
    def __repr__(self):
        string_data = super().__repr__()
        string_data += (f"Name: {self.firstname} {self.lastname} ")
        return string_data