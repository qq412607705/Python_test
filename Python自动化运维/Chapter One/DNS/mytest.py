#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Mr.Chen

import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
MX = dns.resolver.query(domain, 'MX')
for i in MX :
    print('MX preference = ', i.preference, 'mail exchanger =', i.exchange)
