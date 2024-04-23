from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://www.google.com/imgres?q=pet%20image%20not%20available&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D810244404467111&imgrefurl=https%3A%2F%2Fwww.facebook.com%2FMC.Pet.Adoption%2F&docid=JlbmGYac3fyaLM&tbnid=YRqvVP2ru7CJVM&vet=12ahUKEwjS5LuZtLaFAxVvGtAFHVTCBpcQM3oECBkQAA..i&w=940&h=788&hcb=2&ved=2ahUKEwjS5LuZtLaFAxVvGtAFHVTCBpcQM3oECBkQAA"

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False,
                     unique=True)
    species = db.Column(db.Text,
                        nullable=False)
              
    imgUrl = db.Column(db.Text,
                       nullable= True
                       )           
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable= True)
    available = db.Column(db.Boolean,
                          nullable= False,
                          default= True)
    
    def image_url(self):
        """Returns image for pet"""

        return self.imgUrl or DEFAULT_IMAGE
    
def connect_db(app):
        """Connect database to app"""

        db.app = app
        db.init_app(app)

