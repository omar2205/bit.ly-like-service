import os
from bottle import Bottle, response, redirect
from services.URLShortenerService import URLShortenerService

r = Bottle()

@r.route('/<uid>')
def redirect_to_url(uid):
  url = URLShortenerService().get_url(uid)

  if url:
    redirect(url, code=302)

  response.status = 404
  return {
    'code': 404, 'error': 'Not Found',
  }
