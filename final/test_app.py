from fastapi.testclient import TestClient
import app

client = TestClient(app.app)


def test_predict():
    response = client.post(
        '/predict',
        json={"Pclass": 3, "Sex": "male", "Age": 22.0},
    )
    assert response.status_code == 200
    assert 'prediction' in response.json()
