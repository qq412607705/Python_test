#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            print (j.address)
