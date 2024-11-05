import sys
import os
import pytest

# sys.path.insert(0, '/Users/mengsrun/Desktop/csc342_project/MrPresident/app')
# os.chdir('/Users/mengsrun/Desktop/csc342_project/MrPresident/app')

current_path = os.path.abspath(os.getcwd())
proj_path = os.path.dirname(current_path)
app_path = os.path.join(proj_path, 'app')
sys.path.insert(0, app_path)
os.chdir(app_path)

from app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_quizGame(client):
    response = client.get("/game")
    assert response.status_code == 200

def test_about(client):
    response = client.get("/about")
    
    #assert the response and data passed 
    assert response.status_code == 200
    assert b"About_Page" in response.data  

def test_home(client):
    response = client.get("/home")

    assert response.status_code == 200
     #assert the response and data passed 
    assert b"Home_President" in response.data  

def test_presidentData(client):
    # Test the /pres route to ensure it returns JSON data
    response = client.get("/pres")
     #assert the response and data types
    assert response.status_code == 200
    assert response.is_json  

    #Get data and do further test
    data = response.get_json()
  
    assert isinstance(data, dict)
    assert "1" in data  
    assert "46" in data
    assert "47" not in data
    assert "33" in data

    # Check for keys within the first president's data
    first_president = data["1"]
    last_president = data["46"]
    fortyfour_president = data["44"]

    expected_keys = {
        "No", "Name", "Term Years", "Vice President", "First Lady",
        "Party", "Birth-Death ", "IMG filepath", "Description"
    }
    missing_keys = set(expected_keys) - set(first_president)
    assert not missing_keys

    assert first_president["Name"] == "George Washington"
    assert first_president["Vice President"] == "John Adams"
    assert first_president["Party"] == "None "

    assert last_president["Name"] == " Joe Biden"
    assert last_president["Vice President"] == "Kamala Harris"
    assert last_president["Party"] == "Democratic"
   
    assert fortyfour_president["Name"] == " Barack Obama"
    assert fortyfour_president["Vice President"] == "Joe Biden"
    assert fortyfour_president["Party"] == "Democratic"
    

    

