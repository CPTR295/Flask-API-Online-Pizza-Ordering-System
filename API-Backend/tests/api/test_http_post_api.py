import pytest
from main import app as flask_app


@pytest.fixture
def client():
   with flask_app.test_client() as client:
       yield client
       
@pytest.fixture   
def order_data():
    order_details = {"date_ordered": "2020-12-10", "empid": "EMP-101" , "cid": "CUST-101", "oid": "ORD-910"}
    return order_details


def test_add_order(client, order_data):
    res = client.post("/order/add", json=order_data)
    assert res.status_code == 201
    assert res.content_type == 'application/json'