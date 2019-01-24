#!/usr/bin/env python

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import HTTP_HEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Newdefend Web Application Firewall (Newdefend)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, _ = get_page(get=vector)
        retval = re.search(r"NewDefend", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
        retval |= any(_ in (page or "") for _ in ("/nd_block/", "http://www.newdefend.com/feedback/misinformation/"))
        if retval:
            break

    return retval