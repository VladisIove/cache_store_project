import uuid
import unittest
from time import sleep

from cache_store import CacheStore

class TestCacheStore(unittest.TestCase):
  
    def setUp(self):
        self.cache = CacheStore(capacity=2, ttl=1)
        self.request = type('TestRequest', (), {'method': 'GET', 'path': '/'})
        
    def test_cached_function(self): 
        uuid4_1 = self.cache.get(self._generate_uuid4_for_test, self.request)
        sleep(0.5)
        uuid4_2 = self.cache.get(self._generate_uuid4_for_test, self.request)
        self.assertEqual(uuid4_1, uuid4_2)
        sleep(0.5)
        uuid4_3 = self.cache.get(self._generate_uuid4_for_test, self.request)
        self.assertNotEqual(uuid4_1, uuid4_3)

    def test_cached_function_with_force_put(self):
        uuid4_1 = self.cache.get(self._generate_uuid4_for_test, self.request)
        uuid4_2 = self.cache.put(f'{self.request.method}_{self.request.path}', self._generate_uuid4_for_test(self.request))
        self.assertNotEqual(uuid4_1, uuid4_2)

    def _generate_uuid4_for_test(self, args):
        return  f'{uuid.uuid4().hex}-{args}'

if __name__ == '__main__':
    unittest.main()