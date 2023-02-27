import pytest


@pytest.fixture
def set_up():
    print('\n__Start test__')
    yield
    print('__Finish test__')


@pytest.fixture
def data():
    email = 'alexander.risk1996@gmail.com'
    password = 'alexander.risk1996'
    return {"email": email, "password": password}
