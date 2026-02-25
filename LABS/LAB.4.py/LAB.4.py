
login_records = [
    ("neo", "success"),
    ("trinity", "failed"),
    ("trinity", "failed"),
    ("morpheus", "success"),
    ("trinity", "failed"),
    ("neo", "failed"),
    ("smith", "failed"),
    ("smith", "failed"),
    ("smith", "failed")
]

print("Monitoring access to the Matrix...")

failure_log = {}

for user, result in login_records:
    if result == "failed":

        if user in failure_log:
            failure_log[user] += 1
        else:
            failure_log[user] = 1


for user in failure_log:

    if failure_log[user] >= 3:
        print(" SECURITY ALERT:", user, "triggered intrusion protocol!")
print("Matrix security scan finished")

devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

risky_ports = [21, 23, 3389]

print("Scanning network devices...")

risk_count = 0

for ip, ports in devices:
    for port in ports:
        if port in risky_ports:
            print("WARNING:", ip, "has risky port", port, "open")
            risk_count += 1

print("Scan complete:", risk_count, "security risks found")


user_passwords = [
    "Dragon7",
    "UltraSecure99",
    "cat",
    "ShadowHunter1",
    "ALLUPPERCASE123"
]

print("Running password strength protocol...")
secure = 0
insecure = 0


for pwd in user_passwords:

    problems = []

    if len(pwd) < 8:
        problems.append("Too short")


    upper = False
    lower = False
    number = False


    for letter in pwd:

        if letter.isupper():
            upper = True

        elif letter.islower():
            lower = True

        elif letter.isdigit():
            number = True


    if not upper:
        problems.append("Missing uppercase")

    if not lower:
        problems.append("Missing lowercase")

    if not number:
        problems.append("Missing number")


    if len(problems) == 0:

        print("STRONG:", pwd)

        secure += 1

    else:

        print("WEAK:", pwd, "-", ", ".join(problems))

        insecure += 1


print("Final Report:", secure, "secure,", insecure, "insecure")
