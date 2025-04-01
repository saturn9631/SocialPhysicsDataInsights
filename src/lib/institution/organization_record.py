import numpy as np
import pandas as pd
import networkx as nx

from data.actor import Actor

class Organization(Actor):
    def __init__(self, data):
        if type(data) == pd.DataFrame:
            for index, entry in data.iterrows():
                
