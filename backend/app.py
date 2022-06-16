import os
from bottle import Bottle
if os.environ.get('ENV') != 'prod':
  from dotenv import load_dotenv; load_dotenv()

from api import v1

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 4000))
ENV = os.getenv('ENV', 'dev')

main_app = Bottle()

if __name__ == '__main__':
  is_dev = ENV == 'dev'

  main_app.mount('/api/v1/', v1)

  main_app.run(
    host=HOST, 
    port=PORT, 
    debug=is_dev,
    reloader=is_dev
  )