from ast import parse
from http.server import BaseHTTPRequestHandler
from platform import platform
from urllib.parse import urlparse
import platform


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    url = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url.query)
    dic = dict(query_string_list)

    name = dic.get('name')

    if name:
      message = f"Hi {name}"
    else:
      message = f"Hi stranger"

      message += f"\nGreetings from python version {platform.python_version()}"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())
    return