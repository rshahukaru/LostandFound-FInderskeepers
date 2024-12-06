from app.models import Item, Match, db

def find_matches():
    lost_items = Item.query.filter_by(type='lost').all()
    found_items = Item.query.filter_by(type='found').all()

    for lost_item in lost_items:
        for found_item in found_items:
            if (
                lost_item.category == found_item.category and
                lost_item.location == found_item.location and
                abs((lost_item.date_lost_found - found_item.date_lost_found).days) <= 7
            ):
                existing_match = Match.query.filter_by(
                    lost_item_id=lost_item.id,
                    found_item_id=found_item.id
                ).first()

                if not existing_match:
                    match = Match(lost_item_id=lost_item.id, found_item_id=found_item.id)
                    db.session.add(match)
                    db.session.commit()
                    print(f"Match created: Lost Item ID {lost_item.id} - Found Item ID {found_item.id}")
