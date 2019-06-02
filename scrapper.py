import numpy as np
import pandas as pd
import requests
from lxml import html
import parser_config as cfg

def Parse(url):
        page = requests.get(url)
        tree = html.fromstring(page.content)

        l = tree.xpath('//table[@class="fund-snapshot-port-holdings-equity"]//td//text()')

        l = list(filter(lambda x: not x.isspace(), l))

        final = np.reshape(np.array(l), (-1, 6))

        fname = cfg.GetFileName(url.split('=')[-1])
        pd.DataFrame(final).to_csv(fname, header=cfg.header)
        return fname

for fund in cfg.funds:
	print "Done parsing:", fund, "Wrote:", Parse(cfg.funds[fund])

