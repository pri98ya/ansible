''' by using paramiko execute some router commands to analyze  the health
and send the report to the end-user '''

# Required packages
from botlogs import setup_logger
import establish_connection as ec
import os
import ping_device
import argparse
from execute_command_on_nw_device import execute_commands
import Write_CSV_Excel

def main():
    # Accept Parameters at runtime using argparse module
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostname", type=str, help="Enter Hostname",
                        nargs='?', const=0)
    parser.add_argument("--username", type=str, help="Enter Username",
                        nargs='?', default=None, const=0)
    parser.add_argument("--password", type=str, help="Enter Password",
                        nargs='?', default=None, const=0)
    args = parser.parse_args()
    hostname = args.hostname
    username = args.username
    password = args.password
    print(hostname,username,password)
    # Execution of command function and log writing is starting
    print(('*'*10 + 'Health Check started for router {0}' + '*'*10).format(hostname))
    logger1 = setup_logger(os.path.basename(__file__)[:-3])
    logger1.info(('*'*10 + 'Health Check started for router {0}' + '*'*10).format(hostname))
    ping_status, err = ping_device.PingPortCheck(hostname)
    if err:
        print(err)
        logger1.error(err)
    elif ping_status:
        ssh, con_err = ec.ssh_connection(hostname, username, password)
        if con_err:
            print(con_err)
            logger1.error(con_err)
            return False
        else:
            logger1.info("Connection Established with Router {0}".format(hostname))
            commands = ["hostname", "ifconfig", "Show track brief"]
            execution_status = execute_commands(ssh, hostname, logger1, commands)
            if execution_status:
                file_status = Write_CSV_Excel.write_csv(execution_status[1])
                if file_status[0]:
                    logger1.info("File is generated Successfully")
                    return True
                else:
                    logger1.error(file_status[1])
                    return False
    else:
        print("Failed to Ping device {0}".format(hostname))
        logger1.info("Failed to ping device {0}".format(hostname))


# Start program execution
main()