import time

from common.cache_store import cache

def cache_requests(get_response):
    def middleware(request):
        return cache.get(get_response, request)
    return middleware