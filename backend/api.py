import os
from bottle import Bottle, response, request
from services.URLShortenerService import URLShortenerService

v1 = Bottle()

@v1.route('/healthcheck')
def healthcheck():
    return {
      'status':'OK', 
      'env': os.environ.get('ENV')
    }

@v1.route('/create', method='POST')
def url_shortener():
    url = request.json.get('url', None)
    expires = request.json.get('expires', None)

    if not url:
      response.status = 400
      return { 'code': 400, 'error': 'URL is required', 'data': False }
    
    uid = URLShortenerService().add_url(url, expires)

    if uid:
      response.status = 201
      return { 'code': 201, 'error': False, 'data': { 'uid': uid } }
    
    response.status = 500
    return { 'code': 500, 'error': 'Internal Server Error' }


@v1.route('/get/<uid:re:[a-zA-Z0-9_]{6}>')
def redirect_to_url(uid):
  url = URLShortenerService().get_url(uid)

  if url:
    return { 
      'code': 200, 'error': False, 
      'data': {
        'url': url
      }
    }
  response.status = 404
  return {
    'code': 404, 'error': 'Not Found',
  }


@v1.route('/alpha')
def alpha():
  u = URLShortenerService().add_hash('UI!!')
  return {'okay'}

@v1.route('/<url:re:.+>')
def not_found(url):
  response.status = 404
  return { 'code': 404, 'error': 'Not Found' }