import falcon
from falcon import testing
import pytest

from src.server import api

# this @ augment header will create an object at run time,
# here the object is the falcon build-in http client simulator, which will be used in the testing logic to interace with <api>
@pytest.fixture
def client():
    return testing.TestClient(api)


# the <pytest> magic: pytest will run all test_xxx or xxx_test functions in the target directory/python files
# so the test function name must defined as <test_...>, here we use the pytest augmented <client> object, which is 
# the falcon build-in http client simulator
def test_place_api (client):
    place = {
        'county': "my country",
        'state': "my state",
        'city': "my city",
        'street_addr': "123 my street"
    }
    response = client.simulate_get('/')
    assert response.headers['content-type'] == 'application/json; charset=UTF-8'
    assert response.status == falcon.HTTP_OK
    assert response.content == place
