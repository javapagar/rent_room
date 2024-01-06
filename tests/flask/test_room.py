import json
from unittest import mock


rooms = [
            {
                'uuid': 'd3b92e03-b078-4c90-90cd-dcbf59773082', 
                'price': 100, 
                'size': 35, 
                'lon': 2.192227263271727, 
                'lat': 41.396929478820866
            }
        ]

@mock.patch("flask_api.rest.room.RoomListGetter.get_all")
def test_get(mock_use_case,client):
    
    mock_use_case.return_value = json.dumps(rooms)

    http_response = client.get("/rooms")


    assert json.loads(http_response.data.decode("utf-8")) == json.dumps(rooms)
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
