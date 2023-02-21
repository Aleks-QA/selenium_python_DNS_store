import pytest


@pytest.fixture
def set_up():
    print('\n__Start test__')
    yield
    print('__Finish test__')



