from core.jwt_handler import create_JWT_Token,decode_JWT_token


token = create_JWT_Token('123')
print(f'JWT TOKEN IS:{token}')

decode_token = decode_JWT_token(token)
print(f"YOUR DECODE TOKEN IS:{decode_token}")