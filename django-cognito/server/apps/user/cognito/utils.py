import hashlib
import hmac
import base64

from server.apps.user.cognito import constants


def get_cognito_secret_hash(username: str) -> str:
    message = username + constants.CLIENT_ID
    digest = hmac.new(str(constants.CLIENT_SECRET).encode('UTF-8'), msg=str(message).encode('UTF-8'),
                      digestmod=hashlib.sha256).digest()

    return base64.b64encode(digest).decode()
