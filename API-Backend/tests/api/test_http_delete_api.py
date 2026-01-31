import pytest
from main import app as flask_app 
@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client 

def test_delete_order(client):
    res = client.delete('/order/delete/ORD-910')
    assert res.status_code == 201