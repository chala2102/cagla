import logging
import random
from datetime import datetime


log_filename = "analyzer_log_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


ips = ["192.168.1.10", "10.0.0.5", "172.16.0.1", "192.168.1.20"]
requests_list = [
    'GET /index.html HTTP/1.1',
    'POST /login HTTP/1.1',
    'GET /admin HTTP/1.1',
    'POST /submit HTTP/1.1'
]
status_codes = ["200", "401", "403", "404", "500"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "curl/7.68.0",
    "sqlmap/1.6",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

log_file_name = "server_log.txt"

with open(log_file_name, "w") as f:
    # Normal and error logs
    for _ in range(10):
        ip = random.choice(ips)
        request = random.choice(requests_list)
        status = random.choice(status_codes)
        ua = random.choice(user_agents)
        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
        line = f'{ip} - - [{timestamp}] "{request}" {status} 123 "-" "{ua}"\n'
        f.write(line)

    # Failed login attempts (brute force)
    brute_force_ip = "10.0.0.99"
    for _ in range(5):
        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
        line = f'{brute_force_ip} - - [{timestamp}] "POST /login HTTP/1.1" 401 123 "-" "Mozilla/5.0"\n'
        f.write(line)

    # Suspicious user agents
    suspicious_ip = "192.168.1.50"
    for ua in ["curl/7.68.0", "sqlmap/1.6"]:
        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")
        line = f'{suspicious_ip} - - [{timestamp}] "GET /index.html HTTP/1.1" 200 123 "-" "{ua}"\n'
        f.write(line)

print(f"{log_file_name} generated with mock log entries.")


try:
    http_errors_count = 0
    failed_logins_count = 0
    brute_force_ips = {}
    suspicious_ips = set()

    with open(log_file_name, "r") as logfile, \
         open("error_log.txt", "w") as error_file, \
         open("security_incidents.txt", "w") as security_file:

        print("Analyzing logs...")
        failed_logins = {}

        for line in logfile:
            try:
                parts = line.split('"')
                if len(parts) < 6:
                    logging.warning("Unexpected log format: " + line.strip())
                    continue

                ip = parts[0].split()[0]
                request = parts[1]
                status_code = parts[2].split()[0]
                user_agent = parts[5]

                # -------- ERROR LOG --------
                if status_code.startswith("4") or status_code.startswith("5"):
                    error_file.write(line)
                    http_errors_count += 1
                    logging.warning("HTTP Error found: " + line.strip())

                # -------- FAILED LOGIN --------
                if "/login" in request and status_code == "401":
                    security_file.write("Failed login from " + ip + "\n")
                    failed_logins_count += 1
                    logging.warning("Failed login attempt from " + ip)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1

                # -------- SUSPICIOUS USER AGENT --------
                if "curl" in user_agent.lower() or "sqlmap" in user_agent.lower():
                    security_file.write("Suspicious user agent from " + ip + "\n")
                    suspicious_ips.add(ip)
                    logging.warning("Suspicious user agent: " + ip)

            except Exception:
                logging.error("Error parsing line: " + line.strip())

        # -------- BRUTE FORCE DETECTION --------
        for ip, count in failed_logins.items():
            if count >= 3:
                security_file.write(f"Brute force detected from {ip} ({count} attempts)\n")
                brute_force_ips[ip] = count
                logging.warning("Brute force attack from " + ip)

    print("Analysis complete.")
    print("Check error_log.txt for HTTP errors.")
    print("Check security_incidents.txt for security incidents.")

    # ---------- SUMMARY ----------
    print("\n=== Summary ===")
    print(f"Total HTTP errors: {http_errors_count}")
    print(f"Total failed login attempts: {failed_logins_count}")
    if brute_force_ips:
        print(f"Brute force IPs: {', '.join(brute_force_ips.keys())}")
    else:
        print("Brute force IPs: None")
    if suspicious_ips:
        print(f"Suspicious user agents from IPs: {', '.join(suspicious_ips)}")
    else:
        print("Suspicious user agents: None")

except FileNotFoundError:
    print("Log file not found.")
    logging.error(f"{log_file_name} not found.")

except PermissionError:
    print("Permission denied.")
    logging.error("Permission error.")