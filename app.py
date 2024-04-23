from flask import Flask, render_template, redirect,url_for, jsonify
from models import db, connect_db, Pet
from Forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:aniya123@localhost:5432/ADOPTION-AGENCY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "MyBestFriend"


connect_db(app)
with app.app_context():
    db.create_all()

@app.route("/")
def list_pets():
    """List all pets."""

    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect(url_for('list_pets'))

    else:
        
        return render_template("add_pet_form.html", form=form)






@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        
        db.session.commit()
        
        return redirect(url_for('list_pets'))

    else:
        
        return render_template("pet_edit_form.html", form=form, pet=pet)








if __name__== "__main__":
     app.run(debug=True)