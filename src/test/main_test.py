import pandas as pd
import random
from faker import Faker

from lib.game import election
from lib.data import data_filters

def election_test():
    candidate_number = int(input("How many candidates are running?: "))
    candidates = make_people(candidate_number)
    candidates = data_filters.remove_unknown_people(candidates)
    popularity = []
    ideology = []
    for candidate in candidates.iterrows():
        popularity.append(random.randrange(0,11))
        ideology.append(random.randrange(0,11))
    candidates["Popularity"] = popularity
    candidates["Ideology Score"] = ideology

    influencer_number = int(input("How many influencers are interested in the election?: "))
    influencers = make_people(influencer_number)
    influencers = data_filters.remove_unknown_people(influencers)
    popularity = []
    ideology = []
    for influencer in influencers.iterrows():
        popularity.append(random.randrange(0,11))
        ideology.append(random.randrange(0,11))
    influencers["Popularity"] = popularity
    influencers["Ideology Score"] = ideology
    influencers["Endorsed Candidate"] = candidates["Name"][random.randrange(0, len(candidates["Name"]))]
    influencers["Condemned Candidate"] = candidates["Name"][random.randrange(0, len(candidates["Name"]))]

    legislator_number = int(input("How many legislators are there?: "))
    legislators = make_people(legislator_number)
    legislators = data_filters.remove_unknown_people(legislators)
    popularity = []
    ideology = []
    for legislator in legislators.iterrows():
        popularity.append(random.randrange(0,11))
        ideology.append(random.randrange(0,11))
    legislators["Popularity"] = popularity
    legislators["Ideology Score"] = ideology
    legislators["Endorsed Candidate"] = candidates["Name"][random.randrange(0, len(candidates["Name"]))]
    legislators["Condemned Candidate"] = candidates["Name"][random.randrange(0, len(candidates["Name"]))]

    print(f"Here are the candidates:\n{candidates}\n Here are the influencers:\n{influencers}\n Here are the legislators:\n{legislators}\n")
    print("Running election\n")
    result = election.simulate_election(candidates, legislators, influencers)
    print(f"The result of the elections is {result}\n")


def make_people(people_number):
    data = {};
    faking = Faker()
    genders = []
    names = []
    addresses = []
    for i in range(people_number):
        gender = random.randrange(4)
        if gender == 0:
            genders.append("Unknown")
            names.append("N/A")
        elif gender == 1:
            genders.append("Non-Binary")
            names.append(faking.name_nonbinary())
        elif gender == 2:
            genders.append("Female")
            names.append(faking.name_female())
        else:
            genders.append("Male")
            names.append(faking.name_male())
        addresses.append(faking.address())
    data.update({ "Name" : names, "Gender" : genders, "Address" : addresses })
    data = pd.DataFrame(data)
    #print(f"Here is the resulting data\n{data}")
    return data
