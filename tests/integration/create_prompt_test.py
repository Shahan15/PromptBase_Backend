import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch,MagicMock
from app.main import app
from app.core.security import get_current_user

testClient = TestClient(app)

def mock_get_current_user():
    return {'id':'1231231'}

@patch("app.services.gemini_client.GeminiClient")
def test_create_prompt(mock_gemini):
    mock_gemini.return_value.generateOptimisedPrompt.return_value = "Fake optimised prompt"
    
    app.dependency_overrides[get_current_user] = mock_get_current_user

    post_call = testClient.post('/refine',json={"original_prompt":"Generate a fake prompt for me"})
    assert post_call.status_code == 201