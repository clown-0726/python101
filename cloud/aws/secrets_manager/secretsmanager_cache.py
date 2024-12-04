import json
import os
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

"""
Doc refer:
https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-python.html
"""

cache = SecretCache(config=SecretCacheConfig(),
                    client=botocore.session.get_session().create_client('secretsmanager'))

secret = cache.get_secret_string('insight/prod')
secret_obj = json.loads(secret)

print(secret_obj)
