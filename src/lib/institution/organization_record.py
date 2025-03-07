import numpy as np
import pandas as pd
import networkx as nx

from data.actor import Actor

class Organization(Actor):
    def __init__(self, name, constituents):
        __super__(self, name)
        self.sub_orgs = []
        self.members = []
        self.leaders = []
        for constituent in constituents:
            if type(constituent) == Organization:
                self.sub_orgs.append(constituent)
            else:
                self.members.append(constituent)
                if constituent["Leader"] == True:
                    self.leaders.append(constituent)


