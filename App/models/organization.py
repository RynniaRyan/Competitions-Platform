from App.database import db
from App.models import User
from sqlalchemy import ARRAY

# CONSIDERATIONS:
# For example, you may want to add a validation to ensure that the 
# website attribute is a valid URL, or that the social_media_links 
# attribute is a list of valid URLs.

class Organization(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    description = db.Column(db.String(500), nullable=True)
    contact_info = db.Column(db.String(50), nullable=False)
    media_links = db.Column(ARRAY(db.String(255)), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'organization'
    }

    def __init__(self, username, email, password, description, contact_info, role = 'organization', logo=None, media_links=None):
        super().__init__(username, email, password, role)
        self.description = description
        self.contact_info = contact_info
        self.media_links = media_links
    
    def get_json(self):
        json_data = super().get_json()
        json_data.update({
            'description': self.description,
            'contact_info': self.contact_info,
            'logo': self.logo,
            'media_links': self.media_links
        })
        return json_data

    def __repr__(self):
        string_data = super().__repr__()
        string_data += (f"Description: {self.description} | "
                        f"Contact Info: {self.contact_info} | "
                        f"Logo: {self.logo} | "
                        f"Media Links: {self.media_links}")
        return string_data
