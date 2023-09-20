''' Establish the connection with the remote server using the Paramiko module
and return the connection object to the called function or .py file '''

import paramiko


def ssh_connection(hostname, username=None, password=None):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, username=username, password=password, port=22)
        print("Connection established with {0}".format(hostname))
        return ssh_client, None
    except Exception as e:
        #print("Connection failed")
        return None, str(e)
ssh_connection("abc")