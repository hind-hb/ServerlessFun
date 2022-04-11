from http.server import BaseHTTPRequestHandler
from platform import platform
from unicodedata import name
from urllib import parse
from datetime import datetime , date 

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    urlcomponent = parse.urlsplit(s)
    qslist = parse.parse_qsl(urlcomponent.query)
    dice = dict(qslist)
    wlcm = dice.get("wlcm")
    
    if wlcm :
        message = f"\hello {wlcm}"
    else :
        message = "GooD Morning "
    
    message = f"\n   {wlcm} hind {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())




    return
