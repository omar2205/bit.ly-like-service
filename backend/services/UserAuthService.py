import json
from models.UserModel import User
from services import RedisService

class UserAuthService(RedisService):
  def add_user(self, name: str, email: str) -> str:
    # check user's email first
    user = self.get_user_by_email(email)
    if user:
      return '-1'
    new_user = User(name, email)
    self.r.hset(new_user.uid, mapping=new_user.__dict__)
    self.r.set(new_user.token, new_user.uid)
    return new_user.token

  def get_user_by_id(self, uid: str) -> User:
    user_dict = self.r.hgetall(uid) # get the user's dict
    return {**user_dict}


  def get_user_by_token(self, token: str) -> User:
    '''Get a user by their token'''
    user_id = self.r.get(token)
    return self.get_user_by_id(user_id)

  def get_user_by_email(self, email: str) -> User:
    '''Get a user by their email'''
    for user_id in self.r.keys('USER*'):
      user = self.get_user_by_id(user_id)
      if user['email'] == email:
        return user

  def revoke_user_token(self, user_id: str) -> None:
    '''Revoke a user's token'''

    user = self.get_user_by_id(user_id)
    user = User(uid=user['uid'], name=user['name'],
                email=user['email'], token=user['token'])
    
    print('removing user old token', user.token)
    self.r.delete(user.token)

    user.revoke_token()

    self.r.hset(user.uid, mapping=user.__dict__)
    self.r.set(user.token, user.uid)

    return user.token # return the new token

  def revoke_token(self, token: str) -> None:
    '''Revoke a token'''
    user_id = self.r.get(token)
    return self.revoke_user_token(user_id)