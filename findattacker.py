log = [ "1532926994 111.222.333.123 GET /index 200", "1532927014 444.555.666.777 POST /login 401", "1532927240 444.555.666.777 POST /login 401", "1532927335 111.222.333.123 GET /faq 404", "1532927338 111.222.333.123 GET /login 200", "1532927339 111.222.333.123 GET /contact 200", "1532927500 111.222.333.123 POST /login 200", "1532927575 444.555.666.999 POST /login 401"]

failed_login_attempts = {}
for entry in log:
    data = entry.split(" ")
    ip = data[1]
    request = data[3]
    status_code = data[4]
    
    if request == "/login" and status_code == "401":
        if ip in failed_login_attempts:
            failed_login_attempts[ip] += 1
        else:
            failed_login_attempts[ip] = 1

suspect_ips = []
for ip, attempts in failed_login_attempts.items():
    if attempts >= 1:
        suspect_ips.append(ip)

print("Potential attackers: ", suspect_ips)
