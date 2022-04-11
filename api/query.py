from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import random
from random import randint

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    # Generate a way to build a random character
    random_person = str(randint(0, 82)) 
    url = 'https://swapi.dev/api/'
    r = requests.get(url + "/people/" + random_person)
    data = r.json()

    message = str(data)        

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return
