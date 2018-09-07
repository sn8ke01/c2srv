#!/usr/bin/python3

# todo: exit gracefully
# todo: distinguish between OSs for CMD execution

from http.server import HTTPServer, BaseHTTPRequestHandler


class server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/cmd.html'
        try:
            file_to_open = open(self.path[1:]).read()  # File containing cmds
            self.send_response(200)
        except:
            file_to_open = "404 Error"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        '''
        #Use this to receive data back OR have a seperate for capturing CMD output sent from the client  
        '''

    def do_POST(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


def header():
    print('------------------')
    print(' c2http server')
    print('------------------')


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
    port = 8080
    ip = 'localhost'
    header()

    # Server
    httpd = HTTPServer((ip, port), server)
    print("Server running @ {} on port {}".format(ip, port))
    httpd.serve_forever()

    '''
    #http_listener_service()
    get_cmd()
    send_cmd()
    encode_cmd()
    decode_results()
    display_cmd_ouput()
    '''


if __name__ == "__main__":
    main()
