# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "sadeceben"
__github__ = "https://github.com/sadeceben"

from httpx import get
from re import compile


class PassiveDns:
    """passivedns class"""

    def __init__(self):
        """init func."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1"
        }

        self.url = "http://ptrarchive.com/tools/search.htm?label=%s"
        self.passive_reg = compile("<\/td><td>(.*?)<\/td><\/tr>")

    def passive_domain(self, domain_name):
        """passivedns main func."""
        last_data = []
        resp = get(self.url % domain_name, headers=self.headers, timeout=15)
        for line in self.passive_reg.findall(resp.text):
            data = line.split("&nbsp;&nbsp;</td><td>")
            last_data.append({"ip": data[0], "domain": data[-1].split(" ")[0]})

        return last_data
