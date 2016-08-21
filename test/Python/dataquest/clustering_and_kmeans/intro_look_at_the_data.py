#!/usr/bin/env python
import pandas as pd
import numpy as np


# Let's look at the dataset of player performance from the 2013-2014 season.
nba = pd.read_csv("nba_2013.csv")
nba.head(3)