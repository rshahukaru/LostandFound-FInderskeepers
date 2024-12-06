from app import create_app, db
from app.models import User

app = create_app()

def test_auth_setup():
    with app.app_context():
        try:
            # Try to get a user and test password functions
            user = User.query.first()
            if user:
                print(f"Testing with user: {user.name}")
                # Test password hashing
                user.set_password('testpassword')
                assert user.check_password('testpassword'), "Password check failed"
                print("Password hashing works correctly")
                
                # Test login_manager setup
                from flask_login import login_user
                assert hasattr(user, 'is_authenticated'), "UserMixin not properly implemented"
                print("UserMixin properly implemented")
                
                print("\nAuthentication setup is correct!")
                return True
        except Exception as e:
            print(f"Error in auth setup: {str(e)}")
            return False

if __name__ == "__main__":
    test_auth_setup()