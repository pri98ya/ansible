import os


def PingPortCheck(hostname):
    try:
        pingstatus = os.popen('ping -n 1 {}'.format(hostname))
        if 'Packets: Sent = 1, Received = 1' in pingstatus.read():
            print('ping Success!')
            return True,None
        else:
            return False,None
    except Exception as e:
        return False,str(e)
PingPortCheck("hostname")

