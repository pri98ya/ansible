def execute_commands(ssh, hostname, log,commands):
    try:
        device = []
        for cmd in commands:
            cmd_list = []
            cmd_list.append(hostname)
            cmd_list.append(cmd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            std_err = stderr.readlines()
            std_out = stdout.readlines()
            if std_err:
                log.error(std_err)
                cmd_list.append(std_err)
                print("Error:", std_err)
            else:
                log.info(std_out)
                #cmd_list.append(std_out)
                output = str()
                for line in std_out:
                    output = output + line
                cmd_list.append(output)
                if output != "":
                    print(output)
                else:
                    print("There was no output for this command")

            device.append(cmd_list)
        return True,device
    except Exception as e:
        print("Something went wrong for more details please check your logs")
        log.error(str(e)+"on server {0}".format(hostname))
        return False
    finally:
        ssh.close()
