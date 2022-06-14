from nanoid import generate

uid_options = {
  'size': 12,
  'alphabet': '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
}

class User:
  def __init__(self, name, email, uid=None, token=None):
    self.uid = f'USER_{generate(**uid_options)}' if uid is None else uid
    self.name = name
    self.email = email
    self.token = self.generate_token() if token is None else token

  def __repr__(self):
    return f'<User uid:{self.uid} name:{self.name} email:{self.email}>'

  def generate_token(self):
    self.token = f'UA_TOKEN_{generate(uid_options["alphabet"], size=32)}'
    return self.token

  def revoke_token(self):
    self.token = self.generate_token()

# class UserToken:
#   '''UA_Token:User_ID'''
#   def __init__(self, user_id: str):
#     self.user_id = user_id
#     self.token = self.generate_token()

#   def generate_token(self):
#     self.token = f'UA_TOKEN_{generate(uid_options["alphabet"], size=32)}'
#     return self.token

#   def revoke_token(self):
#     self.token = self.generate_token()
#     return self.token
  
#   def __repr__(self):
#     return f'<UA_Token user_id:{self.user_id} token:{self.token}>'
