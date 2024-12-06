from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notification_preferences = db.Column(db.Text)
    
    # Relationships
    items = db.relationship('Item', backref='user', lazy='dynamic')
    claims = db.relationship('Claim', backref='claimer', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Item(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    date_lost_found = db.Column(db.DateTime(timezone=True), nullable=False)
    date_reported = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')
    image_filename = db.Column(db.String(255))

    # Relationships
    claims = db.relationship('Claim', backref='item', lazy='dynamic')

class Claim(db.Model):
    __tablename__ = 'Claims'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('Items.id'), nullable=False)
    claimer_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    proof_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)

class Notification(db.Model):
    __tablename__ = 'Notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Match(db.Model):
    __tablename__ = 'Matches'
    id = db.Column(db.Integer, primary_key=True)
    lost_item_id = db.Column(db.Integer, db.ForeignKey('Items.id'), nullable=False)
    found_item_id = db.Column(db.Integer, db.ForeignKey('Items.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

     # Relationships
    lost_item = db.relationship('Item', foreign_keys=[lost_item_id])
    found_item = db.relationship('Item', foreign_keys=[found_item_id])
