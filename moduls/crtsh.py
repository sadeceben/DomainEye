# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "sadeceben"
__github__ = "https://github.com/sadeceben"

from httpx import get
from re import compile


class CrtSh:
    """crtsh class"""

    def __init__(self):
        """init func."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1"
        }

        self.url = "https://crt.sh/?q=%25."
        self.crtsh_reg = compile("<TD>(.*?)</TD>")

    def crtsh_domain(self, domain_name):
        """crtsh main func."""
        last_data = []

        resp = get(self.url + domain_name, headers=self.headers, timeout=15)
        for line in self.crtsh_reg.findall(resp.text):
            last_data += self.crtsh_parser(line.strip(), domain_name)

        return last_data

    def crtsh_parser(self, link, domain_name):
        """parser func."""
        last_data = []
        subdomains = []
        if "<BR>" in link:
            subdomains = link.split("<BR>")
        else:
            subdomains.append(link)

        for subdomain in subdomains:
            if not subdomain.endswith(domain_name) or "*" in subdomain:
                continue

            if "@" in subdomain:
                subdomain = subdomain[subdomain.find("@") + 1 :]

            if subdomain != domain_name:
                last_data.append(subdomain.strip())

        return last_data
