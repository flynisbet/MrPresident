import sys
import os
import pytest

sys.path.insert(0, '/Users/mengsrun/Desktop/csc342_project/MrPresident/app')
os.chdir('/Users/mengsrun/Desktop/csc342_project/MrPresident/app')

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_some_route(client):
    response = client.get('/about')
    assert response.status_code == 200