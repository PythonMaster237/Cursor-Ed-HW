import requests


def test_get_articles_list():
    response = requests.get("http://localhost:1440/api/articles")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 6
    assert response.json()[1].get("id") == 7


def test_create_article():
    response = requests.post("http://localhost:1440/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    assert response.json().get("title") == "hello"
    res = requests.delete("http://localhost:1440/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_put_article():
    response = requests.post("http://localhost:1440/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    response = requests.put("http://localhost:1440/api/articles/" + str(response.json().get("id")), json={
        "title": "Not hello",
        "body": "Not hello test!"
    })
    assert response.json().get("title") == "Not hello"
    assert response.json().get("body") == "Not hello test!"
    res = requests.delete("http://localhost:1440/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_delete_article():
    response = requests.post("http://localhost:1440/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    res = requests.delete("http://localhost:1440/api/articles/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_get_menu_items_list():
    response = requests.get("http://localhost:1440/api/menu-items")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 1
    assert response.json()[1].get("id") == 2


def test_create_menu_item():
    response = requests.post("http://localhost:1440/api/menu-items", json={
        "name": "news",
        "link": "news about news"
    })
    assert response.status_code == 200
    assert response.json().get("name") == "news"
    res = requests.delete("http://localhost:1440/api/menu-items/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_put_menu_item():
    response = requests.post("http://localhost:1440/api/menu-items", json={
        "name": "hello",
        "link": "hello hello hello"
    })
    assert response.status_code == 200
    response = requests.put("http://localhost:1440/api/menu-items/" + str(response.json().get("id")), json={
        "name": "Not hello",
        "link": "Not hello test!"
    })
    assert response.json().get("name") == "Not hello"
    assert response.json().get("link") == "Not hello test!"
    res = requests.delete("http://localhost:1440/api/menu-items/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_delete_menu_item():
    response = requests.post("http://localhost:1440/api/menu-items", json={
        "name": "hello",
        "link": "hello hello hello"
    })
    assert response.status_code == 200
    res = requests.delete("http://localhost:1440/api/menu-items/" + str(response.json().get("id")))
    assert res.status_code == 204


def test_get_categories_list():
    response = requests.get("http://localhost:1440/api/categories")
    assert response.status_code == 200
    assert response.json()[0].get("id") == 1
    assert response.json()[1].get("id") == 2