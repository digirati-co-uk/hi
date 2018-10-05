import json
import re


def test_get(app):
    """
    Test getting an id
    :param app: Flask applicaiton
    """

    client = app.test_client()

    get_response = client.get('/uuid/new')
    assert get_response.status_code == 200
    new_id = json.loads(get_response.data.decode()).get('id')
    assert is_uuid4(new_id)


def is_uuid4(potential_match):
    return bool(re.match(
        (
            '[a-f0-9]{8}-' +
            '[a-f0-9]{4}-' +
            '4' + '[a-f0-9]{3}-' +
            '[89ab][a-f0-9]{3}-' +
            '[a-f0-9]{12}$'
        ),
        potential_match,
        re.IGNORECASE
    ))
