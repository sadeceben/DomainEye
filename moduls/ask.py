# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "sadeceben"
__github__ = "https://github.com/sadeceben"

from httpx import get
from re import compile


class Ask:
    """Ask class"""

    def __init__(self):
        """init func."""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1"
        }

        self.url = "http://www.ask.com/web?q=%s&page=%i&qid=8D6EE6BF52E0C04527E51F64F22C4534&o=0&l=dir&qsrc=998&qo=pagination"
        self.ask_reg = compile('<p class="PartialSearchResults-item-url">(.*?)</p>')

    def ask_domain(self, domain_name):
        """ask main func."""
        last_data = []
        resp = get(self.url % (domain_name, 0), headers=self.headers, timeout=15)

        for line in self.ask_reg.findall(resp.text):
            last_data.append(line)

        return last_data
