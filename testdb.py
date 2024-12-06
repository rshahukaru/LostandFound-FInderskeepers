from app import create_app, db

app = create_app()

with app.app_context():
    try:
        # Try to create all tables
        db.create_all()
        print("Successfully connected to Azure SQL Database!")
    except Exception as e:
        print("Error connecting to database:")
        print(e)