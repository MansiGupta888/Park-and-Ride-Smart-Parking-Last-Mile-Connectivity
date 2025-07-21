# backend/utils/caching.py
import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def set_cache(key, value, expiry=300):
    cache.set(key, value, ex=expiry)

def get_cache(key):
    return cache.get(key)
