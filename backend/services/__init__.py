import os
import redis

REDIS_URL = os.getenv('REDIS_URL', None)

def get_redis():
  return redis.from_url(REDIS_URL, decode_responses=True)

class RedisService:
  '''r: redis client
  p: redis pipeline'''
  def __init__(self) -> None:
    self.r = get_redis()
    self.p = self.r.pipeline(transaction=True)
    self._complete = False

  def __exit__(self, exc_type, exc_value, traceback):
    self.r.close()
  
  def complete(self):
    self._complete = True

  def close(self):
    if self.p:
      if self._complete:
        self.p.execute()
      else:
        self.p.discard()
      return
    self.r.close()