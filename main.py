from subprocess import DEVNULL, STDOUT, check_call
from faker import Faker
import time
import shlex

requests_amount = 100
fake = Faker()
with open("request.txt", "r") as f:
    curl_request = f.read()

for i in range(requests_amount):
    email = fake.email()
    password = fake.password()
    curl_request = curl_request.replace("tempemail", email)
    curl_request = curl_request.replace("temppassword", password)
    check_call(shlex.split(curl_request), stdout=DEVNULL, stderr=STDOUT)
    print(f"Request {i + 1}/100: Email: {email}, Password: {password}")
    time.sleep(1)
