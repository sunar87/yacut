import random
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from yacut.constants import LENGTH_UNIQUE_ID
from yacut.forms import UrlForm
from yacut.models import URLMap


def get_unique_short_id(length=LENGTH_UNIQUE_ID):
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id


@app.route('/', methods=('GET', 'POST',))
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        if URLMap.query.filter_by(short=custom_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.',
                  'error')
            return render_template('index.html', form=form)
        while (URLMap.query.filter_by(short=custom_id).first()):
            custom_id = get_unique_short_id()
        short_url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(short_url)
        db.session.commit()
        flash(
            url_for(
                'short_link_url', short_id=custom_id, _external=True),
            'complete_link'
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=('GET',))
def short_link_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)