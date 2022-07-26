# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "sadeceben"
__github__ = "https://github.com/sadeceben"

from sys import argv
from moduls.ask import Ask
from moduls.crtsh import CrtSh
from moduls.threatcrowd import ThreatCrowd
from moduls.passivedns import PassiveDns
from templates.templates import START


class DomainEye:
    """Main class."""

    def __init__(self, domain):
        self.domain = domain  # Domain value

        self.passivedns = PassiveDns()  # passivdns engine
        self.crtsh = CrtSh()  # crtsh engine
        self.ask = Ask()
        self.threatcrowd = ThreatCrowd()
        self.subdomains = []

    def main(self):
        """main func."""
        self.subdomains += self.crtsh.crtsh_domain(self.domain)
        self.subdomains += [
            i.get("domain") for i in self.passivedns.passive_domain(self.domain)
        ]
        self.subdomains += self.ask.ask_domain(self.domain)
        self.subdomains += self.threatcrowd.threatcrowd_domain(self.domain)

        self.subdomains = sorted(list(set(self.subdomains)))

        print(START)
        print("\n".join(self.subdomains))  # This func. is write subdomains

        print("\nTotal unique subdomains found: %i" % len(self.subdomains))


if __name__ == "__main__":
    run = DomainEye(argv[1])
    run.main()
