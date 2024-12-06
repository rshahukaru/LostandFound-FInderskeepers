from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Item
from app import db
from datetime import datetime, date
from app.forms import LostItemForm, FoundItemForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    lost_items = Item.query.filter_by(type='lost').order_by(Item.date_reported.desc()).limit(5).all()
    found_items = Item.query.filter_by(type='found').order_by(Item.date_reported.desc()).limit(5).all()
    return render_template('index.html', lost_items=lost_items, found_items=found_items)

@main.route('/lost', methods=['GET', 'POST'])
@login_required
def report_lost():
    form = LostItemForm()
    if form.validate_on_submit():
        date_lost = datetime.combine(form.date_lost.data, datetime.min.time())
        item = Item(
            user_id=current_user.id,
            type='lost',
            title=form.title.data,
            category=form.category.data,
            description=form.description.data,
            location=form.location.data,
            date_lost_found=date_lost,
            status='active'
        )
        db.session.add(item)
        db.session.commit()
        flash('Lost item reported successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('report_lost.html', form=form)

@main.route('/found', methods=['GET', 'POST'])
@login_required
def report_found():
    form = FoundItemForm()
    if form.validate_on_submit():
        date_found = datetime.combine(form.date_found.data, datetime.min.time())
        item = Item(
            user_id=current_user.id,
            type='found',
            title=form.title.data,
            category=form.category.data,
            description=form.description.data,
            location=form.location.data,
            date_lost_found=date_found,
            status='active'
        )
        db.session.add(item)
        db.session.commit()
        flash('Found item reported successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('report_found.html', form=form)

@main.route('/items')
def list_items():
    type_filter = request.args.get('type', 'all')
    category = request.args.get('category', 'all')
    
    query = Item.query
    if type_filter != 'all':
        query = query.filter_by(type=type_filter)
    if category != 'all':
        query = query.filter_by(category=category)
        
    items = query.order_by(Item.date_reported.desc()).all()
    return render_template('items.html', items=items, type_filter=type_filter, category=category)

@main.route('/item/<int:id>')
def item_detail(id):
    item = Item.query.get_or_404(id)
    return render_template('item_detail.html', item=item)