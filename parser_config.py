#!/usr/bin/env python

base_url = 'https://www.valueresearchonline.com/funds/portfoliovr.asp?schemecode='

funds = {'HDFC Small Cap Fund': '16617',
         'L&T Emerging Businesses Fund': '26133'}

header = ['Company', 'Sector', 'PE', '3Y High', '3Y Low', '% Assets']

for i in funds:
	funds[i] = base_url + funds[i]

