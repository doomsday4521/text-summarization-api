import redis
import logging

logger = logging.getLogger(__name__)

class CacheService:
    def __init__(self,url:str):
        try:
            self.client =  redis.Redis.from_url(
                url,
                decode_responses=True
            )
            self.client.ping()
            logger.info("Connected to redis!")
        except Exception as e:
            logger.warning(f"Redis unavalaible: {e}")
            self.client = None


    def get(self,key:str):
        if not self.client:
            return None
        return self.client.get(key)
    def set(self,key:str,value:str,ttl:int):
        if not self.client:
            return
        self.client.setex(key,ttl,value)
        