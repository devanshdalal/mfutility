#!/usr/bin/env python
import pandas as pd

import parser_config

csvs = {}
for mf in parser_config.mutual_funds:
	csvs[mf] = parser_config.GetFileName(parser_config.mutual_funds[mf])


