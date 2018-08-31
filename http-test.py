## Google Test

from c2cli import get_cmd_from_c2http as r
import urllib.request

def main():
	url = 'http://www.google.com'
	port = '443'
  proxy_url = '#######'
  proxy_port = '00000'
  proxy = proxy_url+':'+proxt_port
	
	#proxy object
	proxy = urllib.request.ProxyHandler({'http':proxy })
	# construct a new opener using your proxy settings
	opener = urllib.request.build_opener(proxy)
	# install the openen on the module-level
	urllib.request.install_opener(opener)
	# make a request
	response = urllib.request.urlopen('http://www.google.com')
	x = response.read()
	print(x)
	
	'''
	print('Going to {} on port {}'.format(url, port))
	response = r(url, port)
	print(response)
	'''
	
main()
