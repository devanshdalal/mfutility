import numpy as np
import pandas as pd
import mfconfig as cfg

def PrintArgs(weights):
	print pd.DataFrame({'funds': cfg.parser_config.funds.keys(),
						'weights': weights})

def Analyze(csvs, weights = False):
	if weights == False:
		weights = [1.0/len(csvs)] * len(csvs)
	if len(weights) != len(csvs):
		print len(weights), len(csvs)
		assert False
	PrintArgs(weights)

	funds = []
	for file in csvs:
		funds.append(pd.read_csv(csvs[file]))

	combined = {}
	for i, fund in enumerate(funds):
		for org_details in fund.iterrows():
			org_details = org_details[1]
			company = org_details['Company']
			if company not in combined:
				combined[company] = 0.0
			combined[company] += float(org_details['% Assets']) * weights[i]

	combined = pd.DataFrame(combined.items(), columns=['Company', 'Weight'])
	combined = combined.sort_values(by=['Weight'], ascending=False)
	with pd.option_context('display.max_rows', 100, 'display.max_columns', None):  # more options can be specified also
		print(combined) 


weights = [0.04, 0.1, 0.2, 0.1, 0.3, 0.1, 0.06, 0.1]
Analyze(cfg.csvs, weights)


