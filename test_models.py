from app import create_app, db
from app.models import User, Item, Match, Claim, Notification

app = create_app()

def test_db_connection():
    with app.app_context():
        try:
            # Try to query the Users table
            users = User.query.all()
            print("Successfully connected to database!")
            print(f"Found {len(users)} users")
            return True
        except Exception as e:
            print(f"Database connection error: {str(e)}")
            return False

if __name__ == "__main__":
    test_db_connection()