from dotenv import load_dotenv; load_dotenv()
from services.UserAuthService import UserAuthService

us = UserAuthService()

t = us.add_user('Alice', 'alice@google.com')
# t = us.get_user_by_token('UA_TOKEN_Mf8cWTGb9f9J3aJyxhismW465xUj2fGx')
# t = us.revoke_token('UA_TOKEN_7ajNod1WjDtACk4SObJZi28JdPZUjgSI')
# t = us.revoke_user_token('USER_ID_01aPJRER')
print(t)
# try:
#   print(user)
# except:
#   pass
# us.revoke_user_token('USER_ID_BbBhj08e')