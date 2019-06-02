#!/usr/bin/env python
base_url = 'https://www.valueresearchonline.com/funds/portfoliovr.asp?schemecode='

mutual_funds = {'HDFC Small Cap Fund': '16617',
				'L&T Emerging Businesses Fund': '26133',
				'Reliance Small Cap Fund': '11463',
				'SBI Small Cap Fund': '10603',
				'Axis Small Cap Fund': '22333',
				'Kotak Small Cap Fund': '16382',
				'Franklin India Smaller Companies Fund': '16010',
				'Tata Small Cap Fund': '37989'}

header = ['Company', 'Sector', 'PE', '3Y High', '3Y Low', '% Assets']

funds = {}
for i in mutual_funds:
	funds[i] = base_url + mutual_funds[i]

def GetFileName(id):
	return 'data/' + id + '.csv'

