import re




def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"HTTP/\d\.\d\s+\d{3}\b": "HTTP Status",
        r"IP .* blocked due to potential attack": "HTTP Status",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action",

        # Linux Logs
        r"sshd\[\d+\]: Accepted (password|publickey) for .* from .* port \d+ ssh2": "System Notification",
        r"sshd\[\d+\]: Failed password for .* from .* port \d+ ssh2": "Warning",
        r"kernel: \[.*\] .*": "System Notification",
        r"CRON\[\d+\]: .* \(.*\)": "System Notification",
        r"systemd\[\d+\]: .*start.*": "System Notification",# Matches "Started" "Starting"
        r"systemd\[\d+\]: .*stop.*": "System Notification", # Matches "stopped" "Stopping"
        r"ufs: \[warn\].*": "Warning",
        r"kernel: \[.*\] CPU\d+: .*": "Warning",
        r"kernel: \[.*\] Memory allocation error.*": "Critical Error",
        r"su: (FAILED session|FAILED|session opened) for user .* by .*": "Error",


    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE): # searching pattern from log_message and ignoring uppercase or lower case
            return label
    return "Unknown"





if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))
    print(classify_with_regex("IP 192.168.133.114 blocked due to potential attack"))  # HTTP Status
    print(classify_with_regex("Backup started at 12:00."))
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("System updated to version 1.0.0."))
    print(classify_with_regex("File file1.txt uploaded successfully by user user1."))
    print(classify_with_regex("Disk cleanup completed successfully."))
    print(classify_with_regex("System reboot initiated by user user1."))
    print(classify_with_regex("Test none."))
    print(classify_with_regex("HTTP/1.1 404 Not Found"))

    #Linux Logs
    print(classify_with_regex("sshd[12345]: Accepted password for user1 from 192.168.1.100 port 22 ssh2"))  # Linux Logs
    print(classify_with_regex("sshd[12345]: Failed password for root from 192.168.1.100 port 22 ssh2"))  # Linux Logs
    print(classify_with_regex("kernel: [12345.678910] CPU0: Thermal throttling warning"))  # Linux Logs
    print(classify_with_regex("kernel: [54321.098765] Memory allocation error at 0xdeadbeef"))  # Linux Logs
    print(classify_with_regex("CRON[12345]: (user1) CMD (/usr/bin/backup.sh)"))  # Linux Logs
    print(classify_with_regex("su: session opened for user root by user1(uid=1001)"))  # Linux Logs
    print(classify_with_regex("ufs: [warn] Disk space running low on /dev/sda1"))  # Linux Logs
    print(classify_with_regex("systemd[12345]: Starting Docker Application Container Engine..."))  # Linux Logs
    print(classify_with_regex("systemd[67890]: Stopped Docker Application Container Engine."))  # Linux Logs
    print(classify_with_regex("su: FAILED session for user user1 by root"))  # Linux Logs


