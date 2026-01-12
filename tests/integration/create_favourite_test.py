from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.core.security import get_current_user

testclient = TestClient(app)

def mock_get_current_user():
    return {'id':'1231231'}

@patch("app.routes.favourites.create_favourites.client")
def test_create_favourite(mock_supabase):
    created_prompt_return = [{"id" : "fake-promptID"}]
    created_favourites_return = [{
         "id" : "fake-ID123",
         "created_at" : "2026-01-12T12:00:00",
         "prompt_id" : "fake_prompt_id",
         "user_id" : "fake_User_id"
         }]

    mock_supabase.insert.side_effect = [
        created_prompt_return,
        created_favourites_return
    ]

    requestFavourites_payload = {
        'original_prompt' : 'This is the ORIGINAL prompt',
        'optimised_prompt' : 'This is the OPTIMISED prompt'
    }

  
    app.dependency_overrides[get_current_user] = mock_get_current_user

    post_call = testclient.post('/favourites',json=requestFavourites_payload)
    response_data = post_call.json()

    print(f"\n--- DEBUG DATA ---")
    print(f"Status: {post_call.status_code}")
    print(f"Response JSON: {post_call.json()}")
    print(f"------------------\n")


    assert post_call.status_code == 201
    assert response_data['id'] == created_favourites_return[0]["id"]
    assert response_data['created_at'] == created_favourites_return[0]["created_at"]
    assert response_data['prompt_id'] == created_favourites_return[0]["prompt_id"]
    assert response_data['user_id'] == created_favourites_return[0]["user_id"]

    app.dependency_overrides = {}