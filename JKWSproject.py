# grr074, Grayson Rosequist , 11472931
import json
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample RSA key
rsa_key = {
    "kty": "RSA",
    "kid": "my-key-id",
    "use": "sig",
    "n": "ABC...xyz",  # Your public key modulus (base64url-encoded)
    "e": "AQAB",       # Your public key exponent (base64url-encoded)
    "exp": int(time.time()) + 3600  # Expiry timestamp for the key (example: 1 hour from now)
}

@app.route('/jwks', methods=['GET'])
def jwks():
    # Return the RSA key as the JWKS
    jwks = {"keys": [rsa_key]}
    return jsonify(jwks)

@app.route('/auth', methods=['POST'])
def auth():
    expired = request.args.get('expired', False)

    if expired:
        # Use an expired key for signing
        rsa_key['exp'] = int(time.time()) - 3600  # Expiry timestamp in the past

    # Generate and sign the JWT (not implemented in this example)
    # signed_jwt = generate_jwt(rsa_key)

    return jsonify({"token": "YOUR_GENERATED_JWT"})  # Replace with the actual JWT

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
