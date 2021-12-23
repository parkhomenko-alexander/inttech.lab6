from app import client, app
from flask import url_for
import routes
import pytest


def test_health_route_status_code():
    with app.test_request_context():
        res = client.get(url_for('get_helth'))
        assert res.status_code == 200


def test_health_route_json():
    with app.test_request_context():
        res = client.get(url_for('get_helth'))
        assert res.json == {'env': 'dev'}
