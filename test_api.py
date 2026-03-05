from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validation_error():
    print("--- Testing ai_confidence_score > 1.0 (Should Fail) ---")
    response = client.post(
        "/properties/123/upload-pair",
        json={
            "compliance_id": "comp-123",
            "original_url": "http://example.com/original.jpg",
            "edited_url": "http://example.com/edited.jpg",
            "ai_confidence_score": 1.5
        }
    )
    print("Status Code:", response.status_code)
    print("Response body:", response.json())
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"
    
def test_successful_upload():
    print("\n--- Testing successful upload (Should Pass) ---")
    response = client.post(
        "/properties/123/upload-pair",
        json={
            "compliance_id": "comp-123",
            "original_url": "http://example.com/original.jpg",
            "edited_url": "http://example.com/edited.jpg",
            "ai_confidence_score": 0.95
        }
    )
    print("Status Code:", response.status_code)
    data = response.json()
    print("Response body:", data)
    assert response.status_code == 200, "Expected 200 OK"
    assert "pair_id" in data, "Expected pair_id in response"
    print("Returned pair_id:", data["pair_id"])
    
if __name__ == "__main__":
    test_validation_error()
    test_successful_upload()
    print("\nAll tests passed successfully!")
