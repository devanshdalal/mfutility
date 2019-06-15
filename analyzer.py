import numpy as np
import pandas as pd
import mfconfig as cfg

############################# Helper ######################################

def PrintArgs(csvs, columns = ['file', 'weights']):
    print pd.DataFrame(csvs.items(), columns=columns)

##########################################################################

def WeightedAverage(csvs, columns = ['Stock Invested in', '% of Total Holdings']):
    PrintArgs(csvs, columns)

    funds = []
    for file in csvs:
        funds.append(pd.read_csv(file))

    combined = {}
    for i, fund in enumerate(funds):
        for org_details in fund.iterrows():
            org_details = org_details[1]
            company = org_details[columns[0]]
            if company not in combined:
                combined[company] = 0.0
            combined[company] += float(org_details[columns[1]][:-1]) * weights[i]

    combined = pd.DataFrame(combined.items(), columns = [columns[0], columns[1]])
    combined = combined.sort_values(by=[columns[1]], ascending=False)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(combined)

#############################################################################
# Value research online specific analysis.
#############################################################################
WeightedAverage(cfg.VRO, columns=['Company', '% Assets'])




#############################################################################
# Moneycontrol specific analysis.
#############################################################################
# WeightedAverage(cfg.MC)


