#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
ns = dns.resolver.query(domain, 'NS')
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())