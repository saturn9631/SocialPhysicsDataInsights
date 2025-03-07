import numpy as np
import pandas as pd
import networkx as nx

def search_trait_commonalities(data, trait):
    connections = []
    for target_index, target in data.iterrows:
        for index in (range(target_index, len(data)) + 1):
            if data[index][trait] == target[trait]:
                connections.append((data[
    return result
