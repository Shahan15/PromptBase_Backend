from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.core.security import get_current_user

testClient = TestClient(app)

def mock_get_current_user():
    return {'id':'1231231'}

#TEST FOR CREATION OF PROMPT AND RETURNING PROMPT
@patch("app.routes.prompts.create_prompts.geminiClient")
def test_create_prompt(mock_gemini):
    mock_gemini.generateOptimisedPrompt.return_value = "Fake optimised prompt"
    
    app.dependency_overrides[get_current_user] = mock_get_current_user
    post_call = testClient.post('/refine',json={"original_prompt":"Generate a fake prompt for me"})
    response_data = post_call.json()
    assert post_call.status_code == 201
    assert "original_prompt" in response_data
    assert response_data["optimised_prompt"] == 'Fake optimised prompt'
    #cleaning up dependency overrides
    app.dependency_overrides = {}