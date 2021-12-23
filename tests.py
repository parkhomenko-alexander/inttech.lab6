""" test file """


from flask import url_for
from app import client, app
import routes


def test_health_route_status_code():
    """test route status code"""
    with app.test_request_context():
        res = client.get(url_for("get_helth"))
        assert res.status_code == 200


def test_health_route_json():
    """test route status json"""

    with app.test_request_context():
        res = client.get(url_for("get_helth"))
        assert res.json == {"env": "dev"}
