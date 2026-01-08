from app.core.jwt_handler import create_JWT_Token,decode_JWT_token


def test_create_jwt():
    user_id = 'test@example.com'
    token = create_JWT_Token(user_id)

    decoded_token = decode_JWT_token(token)

    assert isinstance(decoded_token,str),"JWT Token shoul be a str"
    assert len(decoded_token) > 0
    assert decoded_token == user_id,f'decoded JWT Token should be {user_id},recieved: {decoded_token}'

    
