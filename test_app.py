from app import app

client = app.test_client()

def test_home_content():
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome Page" in response.data
    assert b"This is the main home page" in response.data

def test_header_content():
    response = client.get('/header')
    assert response.status_code == 200
    assert b"This is the HEADER" in response.data
    assert b"logo and nav bar" in response.data

def test_body_content():
    response = client.get('/body')
    assert response.status_code == 200
    assert b"This is the BODY section" in response.data
    assert b"main content of the website" in response.data

def test_footer_content():
    response = client.get('/footer')
    assert response.status_code == 200
    assert b"Footer" in response.data
    assert b"All rights reserved" in response.data
