import sys
import os
import pytest

sys.path.insert(0, '/Users/flynnnisbet/Desktop/CSC-342/semesterProject/app')
os.chdir('/Users/flynnnisbet/Desktop/CSC-342/semesterProject/app')

from app import app

@pytest.fixture
def client():
 with app.test_client() as client:
    yield client
 
def test_some_route(client):
 response = client.get('/about')
 assert response.status_code == 200