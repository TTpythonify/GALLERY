import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# User data
name = "John Doe"
password = "password123"

# Hash the password
password_hash = generate_password_hash(password, method='sha256')

# Define the payload
payload = {
    "sub": "1234567890",
    "name": name,
    "password": password_hash,
    "iat": datetime.datetime.utcnow()
}

# Define the secret key
secret = "your-256-bit-secret"

# Encode the JWT
token = jwt.encode(payload, secret, algorithm="HS256")

print(token)
