from http.client import CONTINUE
import os
from bottle import Bottle
if os.environ.get('ENV') != 'prod':
  from dotenv import load_dotenv; load_dotenv()

CONTACT_URL = os.environ.get('CONTACT_URL', 'oskr.nl')

from api import v1
from api_redirect import r
from enable_cors import enable_cors

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 4000))
ENV = os.getenv('ENV', 'dev')

main_app = Bottle()

@main_app.route('/')
def home():
  return {
    'code': 200,
    'message': f'Visit {CONTACT_URL} for more information'
  }

if __name__ == '__main__':
  is_dev = ENV == 'dev'

  main_app.mount('/api/v1/', v1)
  main_app.mount('/r/', r)

  main_app.install(enable_cors())
  v1.install(enable_cors())
  r.install(enable_cors())

  main_app.run(
    host=HOST, 
    port=PORT, 
    debug=is_dev,
    reloader=is_dev
  )