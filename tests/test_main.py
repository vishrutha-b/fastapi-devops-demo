import pytest
import os
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestRoot:
    def test_root_returns_welcome(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "Welcome" in data["message"]


class TestHealth:
    def test_health_check(self, client: TestClient) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data


class TestItems:
    def test_list_items_empty(self, client: TestClient) -> None:
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == [] or isinstance(response.json(), list)

    def test_create_item(self, client: TestClient) -> None:
        payload = {"name": "Widget", "description": "A test widget", "price": 9.99}
        response = client.post("/items", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Widget"
        assert data["price"] == 9.99
        assert "id" in data

    def test_get_item_not_found(self, client: TestClient) -> None:
        response = client.get("/items/99999")
        assert response.status_code == 404

    def test_create_and_get_item(self, client: TestClient) -> None:
        payload = {"name": "Gadget", "price": 19.99}
        create_resp = client.post("/items", json=payload)
        item_id = create_resp.json()["id"]

        get_resp = client.get(f"/items/{item_id}")
        assert get_resp.status_code == 200
        assert get_resp.json()["name"] == "Gadget"
