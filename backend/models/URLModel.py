from nanoid import generate

uid_options = {
  'size': 6,
  'alphabet': '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
}

class URL:
  def __init__(self, url: str, expires: int, owner: str = 'anon') -> None:
    '''expires: in secs'''
    self.uid = generate(**uid_options)
    self.url = url
    self.expires = expires if expires else 259200 # 3 days
    self.owner = owner if owner else 'anon'
    print('[MODELS/URL]', self.uid, self.url, self.expires)

  def __repr__(self):
    return f'<URL uid:{self.uid} url:{self.url} expires:{self.expires} owner:{self.owner}>'