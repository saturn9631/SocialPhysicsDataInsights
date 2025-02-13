import pandas as pd
import torch

#replace legislaq6tors and influencers with winning coalition. Later add selectorate.
def simulate_election(candidates, legislators, influencers):
    results = pd.DataFrame(columns = ["Name", "Win Chances"])
    for index, candidate in candidates.iterrows():
        endorsement_count = -1
        endorsement_list = []

        for index, legislator in legislators.iterrows():
            endorsement = (candidate["Ideology Score"] - legislator["Ideology Score"]) * 10
            if legislator["Endorsed Candidate"] == candidate["Name"]:
                endorsement += 15
            if legislator["Condemned Candidate"] == candidate["Name"]:
                endorsement += -15
            print(f"The legislator {legislator} supports {candidate["Name"]} {endorsement}\n")
            endorsement_list.append(endorsement)

        for index, influencer in influencers.iterrows():
            endorsement = (candidate["Ideology Score"] - influencer["Ideology Score"]) * 10
            if influencer["Endorsed Candidate"] == candidate["Name"]:
                endorsement += 15
            if influencer["Condemned Candidate"] == candidate["Name"]:
                endorsement += -15
            print(f"The legislator {influencer} supports {candidate["Name"]} {endorsement}\n")
            endorsement_list.append(endorsement)
        total_endorsement = sum(endorsement_list)
        print(f"The mean endorsement for {candidate} is {total_endorsement}\n")
        results.loc[len(results.index)] = [ total_endorsement, candidate["Name"] ]
        return results
