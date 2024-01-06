from unittest import mock
from room.infraestructure.memory_reposiory import MemoryRepository

def test_repo_memory_get_all(room_dict_list):
    repo = MemoryRepository(room_dict_list)

    assert room_dict_list == repo.get_all()