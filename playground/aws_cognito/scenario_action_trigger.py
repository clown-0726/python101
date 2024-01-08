from cognito_idp_actions import CognitoIdentityProviderWrapper
import boto3

user_pool_id = ""
client_id = ""
client_secret = ""

cog_wrapper = CognitoIdentityProviderWrapper(
    boto3.client("cognito-idp"),
    user_pool_id,
    client_id,
    client_secret=client_secret
)

cog_wrapper.admin_set_user_password(user_name="admin", password="Welcome!23", permanent=True)

if __name__ == "__main__":
    pass
