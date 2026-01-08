class FakeCache:
    def __init__(self):
        self.store = {}

    def get(self, key: str):
        return self.store.get(key)

    def set(self, key: str, value: str, ttl: int):
        self.store[key] = value


class SpyModel:
    def __init__(self):
        self.call_count = 0

    def summarize(self, text: str) -> str:
        self.call_count += 1
        return "fake summary"

class FakeRedis:
    def __init__(self):
        self.store = {}

    def incr(self, key):
        self.store[key] = self.store.get(key, 0) + 1
        return self.store[key]

    def expire(self, key, ttl):
        pass
