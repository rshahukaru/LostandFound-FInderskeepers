from app import create_app, db
from app.models import User, Item, Match, Claim, Notification

app = create_app()

def test_relationships():
    with app.app_context():
        try:
            # Get first user
            user = User.query.first()
            if user:
                print(f"\nFound user: {user.name}")
                print(f"User's items: {user.items.count()}")
                print(f"User's claims: {user.claims.count()}")
                print(f"User's notifications: {user.notifications.count()}")
                return True
        except Exception as e:
            print(f"Error testing relationships: {str(e)}")
            return False

if __name__ == "__main__":
    test_relationships()