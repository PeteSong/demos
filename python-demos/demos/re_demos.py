"""
Model Name: re_demos.py
Description: re demos
Author: Peter Song
Date: 2025-01-08
Version: 0.0.1
"""

import re

# 定义IPv4的正则表达式
IPV4_PATTERN = (
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
    r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
)

# IPV4_PATTERN_2 = (r"(\d){1,3}\."
#                  r"(\d){1,3}\."
#                  r"(\d){1,3}\."
#                  r"(\d){1,3}")

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def valid_pattern(pattern: str, target: str) -> bool:
    return re.fullmatch(pattern, target) is not None


def search_pattern(pattern: str, s: str) -> str:
    match = re.search(pattern, s)
    if match:
        return match.group(0)
    return ""


def valid_ipv4(ip: str) -> bool:
    return valid_pattern(IPV4_PATTERN, ip)


def valid_email(email: str) -> bool:
    return valid_pattern(EMAIL_PATTERN, email)


def search_ipv4(s: str) -> str:
    return search_pattern(IPV4_PATTERN, s)


def main():  # pragma: no cover
    test_ips = [
        "192.168.1.1",  # 有效
        "255.255.255.255",  # 有效
        "0.0.0.0",  # 有效
        "256.100.50.25",  # 无效
        "192.168.1",  # 无效
        "192.168.1.1.1",  # 无效
        "192.168.abc.1",  # 无效
    ]
    for ip in test_ips:
        print(f"{ip} is valid: {valid_ipv4(ip)}")

    s1 = "Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for user from 192.168.1.2 port 43367 ssh2"
    print(search_ipv4(s1))


if __name__ == "__main__":
    main()
