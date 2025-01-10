import pytest

import demos.re_demos as reds

test_ips_ipv4 = [
    (True, "192.168.1.1"),
    (True, "255.255.255.255"),
    (True, "0.0.0.0"),
    (False, "256.100.50.25"),
    (False, "192.168.1"),
    (False, "192.168.1.1.1"),
    (False, "192.168.abc.1"),
]

test_ips_ipv6 = [
    (True, "2001:0db8:85a3:0000:0000:8a2e:0370:7334"),
    (False, "2001:db8:85a3::8a2e:370:7334"),
    (False, "1200::AB00:1234::2552:7777:1313"),
    (False, "1200:0000:AB00:1234:O000:2552:7777:1313"),
]


@pytest.mark.parametrize("expected, ip", test_ips_ipv4)
def test_valid_ipv4(expected, ip):
    actual_result = reds.valid_ipv4(ip)
    assert expected == actual_result


@pytest.mark.parametrize("expected, ip", test_ips_ipv6)
def test_valid_ipv6(expected, ip):
    actual_result = reds.valid_ipv6(ip)
    assert expected == actual_result


test_emails = [(True, "1@a.com"), (False, "@b")]


@pytest.mark.parametrize("expected, email", test_emails)
def test_valid_email(expected, email):
    actual_result = reds.valid_email(email)
    assert expected == actual_result


test_str_with_ips = [
    (
        "192.168.1.2",
        "Jan 30 11:08:25 prod-db-01 sshd[30067]: Failed password for user from 192.168.1.2 port 43367 ssh2",
    ),
    ("", ""),
]


@pytest.mark.parametrize("expected, s", test_str_with_ips)
def test_search_ipv4(expected, s):
    actual_result = reds.search_ipv4(s)
    assert expected == actual_result
