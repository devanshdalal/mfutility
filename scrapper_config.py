#!/usr/bin/env python
base_url = 'https://www.valueresearchonline.com/funds/portfoliovr.asp?schemecode='
header = ['Company', 'Sector', 'PE', '3Y High', '3Y Low', '% Assets']

# # Small Caps funds in India
mutual_funds_codes = {'HDFC Small Cap Fund': '16617',
                      'L&T Emerging Businesses Fund': '26133',
                      'Reliance Small Cap Fund': '11463',
                      'SBI Small Cap Fund': '10603',
                      'Axis Small Cap Fund': '22333',
                      'Kotak Small Cap Fund': '16382',
                      'Franklin India Smaller Companies Fund': '16010',
                      'Tata Small Cap Fund': '37989'}
weights = [0.04, 0.1, 0.2, 0.1, 0.3, 0.1, 0.06, 0.1]

# Thematic(Infra) funds in India
# mutual_funds_codes = {'Franklin Build India Fund': '10563',
#                       'L&T Infrastructure Fund': '16275',
#                       'Kotak Infrastructure and Economic Reform Fund': '16508',
#                       'BOI AXA Manufacturing & Infrastructure Fund': '15735',
#                       'SBI Infrastructure Fund': '5071',
#                       'Sundaram Infrastructure Advantage Fund': '16138',
#                       'UTI Infrastructure Fund': '15900',
#                       'Invesco India Infrastructure Fund': '16774',
#                       'IDFC Infrastructure Fund': '16514'}
# weights = [0.15, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Thematic(Consumption) funds in India
# mutual_funds_codes = {'Sundaram Rural and Consumption Fund': '16163',
#                       'Tata India Consumer Fund': '31360',
#                       'Mirae Asset Great Consumer Fund': '16584',
#                       'Aditya Birla Sun Life India GenNext Fund': '15834',
#                       'SBI Consumption Opportunities Fund': '17525',
#                       'Quant Consumption Fund': '8827',
#                       'Reliance Consumption Fund': '2474',
#                       'Canara Robeco Consumer Trends Fund': '16600' 
#                      }
# weights = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]

#######################################################################################

MCFunds = [
	'https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/small-cap-fund.html']
