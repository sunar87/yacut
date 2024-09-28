from http import HTTPStatus
import re
import logging

from flask import jsonify, request

from yacut.models import URLMap
from yacut.views import get_unique_short_id
from yacut.handler_errors import InvalidAPIUsage
from yacut.constants import (NO_REQUEST_BODY, REQUIRED_URL, ID_NOT_FOUND,
                             NAME_IS_OCCUPIED, USER_INPUT_LIMIT,
                             INVALID_NAME_FOR_LINK, REEXP_FOR_CUSTOM_ID,
                             REEXP_FOR_URL)
from . import app, db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/api/id/', methods=('POST',))
def add_short_url():
    data = request.get_json(silent=True)
    if data is None:
        logger.error("No request body provided")
        raise InvalidAPIUsage(NO_REQUEST_BODY)

    url_map = URLMap()
    custom_id = data.get('custom_id', None)

    if 'url' not in data:
        logger.error("URL is required")
        raise InvalidAPIUsage(REQUIRED_URL)

    if re.search(REEXP_FOR_URL, data['url']) is None:
        logger.error(f"Invalid URL: {data['url']}")
        raise InvalidAPIUsage('url field must be an address')

    if custom_id and not re.match(REEXP_FOR_CUSTOM_ID, custom_id):
        logger.error(f"Custom ID {custom_id} contains invalid characters")
        raise InvalidAPIUsage(INVALID_NAME_FOR_LINK)

    if not custom_id or custom_id is None:
        custom_id = get_unique_short_id()

    if URLMap.query.filter_by(short=custom_id).first():
        logger.error(f"Custom ID {custom_id} is already occupied")
        raise InvalidAPIUsage(NAME_IS_OCCUPIED.format(custom_id=custom_id))

    if len(custom_id) > USER_INPUT_LIMIT:
        logger.error(f"Custom ID {custom_id} exceeds the length limit")
        raise InvalidAPIUsage(INVALID_NAME_FOR_LINK)

    data.update({'custom_id': custom_id})
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()

    logger.info(f"Short URL created: {custom_id}")
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_short_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is not None:
        return jsonify({'url': url_map.original}), HTTPStatus.OK
    raise InvalidAPIUsage(ID_NOT_FOUND, HTTPStatus.NOT_FOUND)