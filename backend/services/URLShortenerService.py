from models.URLModel import URL
from services import RedisService


class URLShortenerService(RedisService):
  def add_url(self, url: str, expires: int) -> str:
    new_url = URL(url, expires)
    self.r.set(new_url.uid, new_url.url, ex=new_url.expires)
    return new_url.uid

  def get_url(self, uid: str) -> str:
    return self.r.get(uid)

  # def add_hash(self, u):
  #   self.p.hset('hello', mapping={'name': 'world', 'u': u})
  #   self.p.expire('hello', 10)
  #   self.complete() # indicate that we are done with the pipeline
  #   self.close() # commit the pipeline & close the connection