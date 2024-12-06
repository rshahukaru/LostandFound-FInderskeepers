from app import create_app, db
from app.models import User, Item, Match, Claim, Notification
from sqlalchemy import inspect

app = create_app()

def inspect_tables():
    with app.app_context():
        inspector = inspect(db.engine)
        
        # Get all table names
        print("Available tables:")
        for table_name in inspector.get_table_names():
            print(f"\nTable: {table_name}")
            
            # Get columns for each table
            print("Columns:")
            for column in inspector.get_columns(table_name):
                print(f"  - {column['name']}: {column['type']}")

if __name__ == "__main__":
    inspect_tables()