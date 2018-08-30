#!/usr/bin/python3

# todo: listen for http packet requesting commands
# todo: send commnds in an http packet
from http.server import HTTPServer, BaseHTTPRequestHandler


class server(BaseHTTPRequestHandlerx):
	
	def do_GET(self):
		if self.path == '/':
			self.path = '/cmd.html'
		try:
			file_to_open = open(self.path[1:]).read() #File containing cmds
			self.send_response(200)
		except:
			file_to_open = "404 Error"
			self.send_response(404)

		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))


def header():
    print('------------------')
    print(' c2http server')
    print('------------------')
    print('0')


def http_listener_service():
    pass


def get_cmd():
    pass


def send_cmd():
    pass


def encode_cmd():
    pass


def decode_results():
    pass


def display_cmd_ouput():
    pass


def main():
    
    '''header()'''
    print('1')
    httpd = HTTPServer(('localhost', 8080), server)
    print('2')
    httpd.serve_forever()
    print("Server running....")
'''
    #http_listener_service()
    get_cmd()
    send_cmd()
    encode_cmd()
    decode_results()
    display_cmd_ouput()
'''
main()
