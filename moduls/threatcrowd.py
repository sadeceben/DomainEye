# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "sadeceben"
__github__ = "https://github.com/sadeceben"

from httpx import get


class ThreatCrowd:
    """threatcrowd class"""

    def __init__(self):
        """init func."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1"
        }

        self.url = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=%s"

    def threatcrowd_domain(self, domain_name):
        """threatcrowd main func."""
        last_data = []
        resp = get(self.url % domain_name, headers=self.headers, timeout=15)

        for line in resp.json().get("subdomains"):
            last_data.append(line)

        return last_data
