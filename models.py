"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User"""
    __tablename__ = 'users'

    icon = '/static/user.png'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(40),
                           nullable=False)
    last_name = db.Column(db.String(40))
    image_url = db.Column(db.String,
                          nullable=False,
                          default=icon)
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.image_url}>"

class Post(db.Model):
    """Post"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(60),
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id', ondelete='SET NULL'))

    user = db.relationship('User', backref='posts')
        
    def __repr__(self):
        return f"<Post {self.title} {self.content} {self.created_at} {self.user_id}>"