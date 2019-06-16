import numpy as np
import pandas as pd
import mfconfig as cfg
import sys
import utils

############################# Helper ######################################

def PrintArgs(csvs, columns = ['instrument', 'weight']):
    print pd.DataFrame(csvs.items(), columns=columns)

##########################################################################

def WeightedAverage(csvs, columns = ['Stock Invested in', '% of Total Holdings']):
    PrintArgs(csvs)

    funds = []
    weights = []
    for file in csvs:
        funds.append(pd.read_csv(file))
        weights.append(csvs[file])
    # print "weights", weights
    # print "funds: ", funds

    combined = {}
    for i, fund in enumerate(funds):
        for org_details in fund.iterrows():
            org_details = org_details[1]
            company = org_details[columns[0]]
            # print org_details[columns[1]], weights[i]
            if company not in combined:
                combined[company] = 0.0
            combined[company] += float(org_details[columns[1]]) * weights[i]

    combined = pd.DataFrame(combined.items(), columns = [columns[0], columns[1]])
    combined = combined.sort_values(by=[columns[1]], ascending=False)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(combined)

# WeightedAverage(cfg.VRO, columns=['Company', '% Assets'])
# WeightedAverage(cfg.MC)

args = utils.ParseCmd(sys.argv)
if args.source is not None:
    #############################################################################
    # Value research online specific analysis.
    #############################################################################
    if utils.MC in args.source:
        WeightedAverage(cfg.MC)        
    #############################################################################
    # Moneycontrol specific analysis.
    #############################################################################
    if utils.VRO in args.source:
        WeightedAverage(cfg.VRO, columns=['Company', '% Assets'])      
