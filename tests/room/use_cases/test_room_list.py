import pytest
from unittest import mock
from room.use_cases.room_list_getter import RoomListGetter


def test_all_room_list(room_list):
    repo = mock.Mock()
    repo.get_all.return_value = room_list
    result = RoomListGetter.get_all(repo)
  
    repo.get_all.assert_called_with()
    assert result == room_list