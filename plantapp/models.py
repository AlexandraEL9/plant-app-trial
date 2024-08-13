from plantapp import db
from datetime import datetime

#table for categories
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True )
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Category {self.category_name}>'

#table for recipes
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f'<Recipe {self.recipe_name}>'
