from app.room.domain.models.room import Room
import pytest 

@pytest.fixture
def room_dict_list():
    rooms = [
        {
            'uuid': 'd3b92e03-b078-4c90-90cd-dcbf59773082', 
            'price': 100, 
            'size': 35, 
            'lon': 2.192227263271727, 
            'lat': 41.396929478820866
        },
        {
            'uuid': 'cd2604d1-fd32-431f-8a2e-d05109d446a9',
            'price': 80,
            'size': 22,
            'lon': -1.9530262180797267,
            'lat': 43.28142779570911
        },
        {
            'uuid': 'f391d9cf-13f8-49bb-9dc4-5c8e9fbb5509', 
            'price': 70, 
            'size': 20, 
            'lon': -4.774087390262258, 
            'lat': 37.89819060042842
        }
    ]
    return rooms
@pytest.fixture
def room_list(room_dict_list):
    return [Room(**room) for room in room_dict_list]