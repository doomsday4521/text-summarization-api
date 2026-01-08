from fastapi import HTTPException,Request

import time

class RateLimiter:
    def __init__(self,redis_client,limit:int,window:int):
        self.redis = redis_client
        self.limit = limit
        self.window = window

    def check(self,request:Request):
        if not self.redis:
            return None
        client_ip = request.client.host
        key = f"rate:{client_ip}"
        current = self.redis.incr(key)
        if current==1:
            self.redis.expire(key,self.window)

        if current>self.limit:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded"
            )