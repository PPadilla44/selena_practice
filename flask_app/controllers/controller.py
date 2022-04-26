from flask_app import app
from flask import redirect, render_template, request, session

from flask_app.models import user, attraction, location

@app.route('/')
def method_name():
    users = user.User.get_all()
    locations = location.Location.get_all()
    attractions = attraction.Attraction.get_all()
    latest = []
    if 'loc_id' in session:
        latest = location.Location.get_all_joined({'id': session['loc_id']})

    return render_template('index.html', users = users, locations = locations, attractions = attractions, latest = latest)

@app.route('/users', methods=['POST'])
def create_user():
    user.User.save(request.form)
    return redirect("/")

@app.route('/locations', methods=['POST'])
def create_all():
    loc_id = location.Location.save({ 'name': request.form['l_name'], 'users_id': 1 })
    session['loc_id'] = loc_id
    attraction.Attraction.save_mult(request.form, loc_id)
    return redirect("/")