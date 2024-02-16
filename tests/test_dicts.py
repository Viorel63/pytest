from utils import dicts


def test_get_val_existing_key():
    collection = {'a': 1, 'b': 2, 'c': 3}
    key = 'b'
    result = dicts.get_val(collection, key)
    assert result == 2


def test_get_val_non_existing_key():
    collection = {'a': 1, 'b': 2, 'c': 3}
    key = 'd'
    result = dicts.get_val(collection, key)
    assert result == 'git'


def test_get_val_with_default():
    collection = {'a': 1, 'b': 2, 'c': 3}
    key = 'd'
    default_value = 10
    result = dicts.get_val(collection, key, default=default_value)
    assert result == default_value
