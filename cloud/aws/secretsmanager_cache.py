import json
import os
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

for key in secret_obj:
    # print(key, secret_obj[key])
    os.environ.setdefault(key, secret_obj[key])

print(os.environ.get("DJANGO_SECRET_KEY"))
