import uuid
import pytest
from app.entities.models.room import Room

@pytest.fixture
def room_dict() ->dict:
    uuid_aux = uuid.uuid4()
    return {
        "uuid": uuid_aux,
        "price": 1100,
        "size" : 55,
        "lon" :-3.697303371164044,
        "lat": 40.39736422960624
    }      

def test_room(room_dict):
    room_model = Room(**room_dict)

    assert room_model.uuid == room_dict["uuid"]
    assert room_model.price == 1100
    assert room_model.size == 55
    assert room_model.lon == -3.697303371164044
    assert room_model.lat == 40.39736422960624

def test_room_to_dict(room_dict):
    room_model = Room(**room_dict)
    
    assert room_dict == room_model.model_dump()

def test_room_compare(room_dict):
    room1 = Room(**room_dict)
    room2 = Room(**room_dict)
    
    assert room1 == room2