#!/usr/bin/env python

funds = {'16617': 0.5,
         '26133': 0.5}

header = ['Company', 'Sector', 'PE', '3Y High', '3Y Low', '% Assets']

for i in funds:
	funds[i] = base_url + funds[i]

