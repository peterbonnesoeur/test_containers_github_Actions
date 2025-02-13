import pytest
from testcontainers.redis import RedisContainer

def test_redis_connection():
    # Start Redis container
    with RedisContainer() as redis:
        # Get the Redis client
        client = redis.get_client()
        
        # Test setting and getting a value
        client.set("test_key", "test_value")
        assert client.get("test_key") == b"test_value" 