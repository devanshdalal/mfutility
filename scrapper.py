import numpy as np
import pandas as pd
import requests
from lxml import html
import xml.etree.ElementTree as ET
import parser_config as cfg

def Parse(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    l = tree.xpath('//table[@class="dataTableId"]//td')

    l = list(filter(lambda x: not x.isspace(), l))

    final = np.reshape(np.array(l), (-1, 6))

    fname = cfg.GetFileName(url.split('=')[-1])
    pd.DataFrame(final).to_csv(fname, header=cfg.header)
    return fname

# for fund in cfg.funds:
# 	print "Done parsing:", fund, "Wrote:", Parse(cfg.funds[fund])

# moneycontrol extract links
def Transform(url):
	url = url.replace('/nav','')
	url = url.split('/')
	return '/'.join(url[:-1] + ['portfolio-holdings'] + [url[-1]])

def ExtractLinks(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    links = tree.xpath('//table[@class="mctable1" and @id="dataTableId"]//a/@href')
    text = tree.xpath('//table[@class="mctable1" and @id="dataTableId"]//a/text()')
    crisil = tree.xpath('//td[@class="crisil_col"]//text()')
    out = list(filter(lambda x: 'direct' in x[0] and (x[2] in ['2', '3', '4', '5']), zip(links, text, crisil)))
    out = map(lambda x: (Transform(x[0]),x[1],x[2]), out)
    return out

def ParseCsv(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    rows = tree.xpath('//table[@id="equityCompleteHoldingTable"]//tr[not(@style)]')[1:]
    rows = map(lambda x: x.xpath('./td//text()'), rows)
    rows = map(lambda x: filter(lambda y: not y.isspace(), x), rows)
    # for x in rows:
    #     print x
    final = np.array(rows)

    fname = cfg.GetFileName(url.split('/')[-3])
    pd.DataFrame(final).to_csv(fname, encoding = 'utf-8')
    return fname

links = ExtractLinks(cfg.MCFunds)
for x in links:
    print x[0], x[1], x[2]
    print ParseCsv(x[0])


# print ParseCsv('https://www.moneycontrol.com/mutual-funds/hdfc-small-cap-fund-direct-plan/portfolio-holdings/MMS025')
