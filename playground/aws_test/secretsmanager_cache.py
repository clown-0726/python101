import json
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

"""
Doc refer:
https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-python.html
"""

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache(config=cache_config, client=client)

secret = cache.get_secret_string('insight/prod')
secret_obj = json.loads(secret)

print(secret_obj)
print(secret_obj["DJANGO_SECRET_KEY"])
