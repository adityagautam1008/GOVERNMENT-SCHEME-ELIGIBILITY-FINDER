import json

def load_schemes():
    with open("schemes.json","r",encoding="utf-8") as f:
        return json.load(f)

def check_eligibility(user, selected_state):

    schemes = load_schemes()
    eligible = []

    for scheme in schemes:

        if scheme["state"]!="All" and scheme["state"]!=selected_state:
            continue

        cond = scheme["conditions"]
        match = True

        for key,value in cond.items():

            if key=="income_max" and user["income"]>value:
                match=False

            if key=="age_min" and user["age"]<value:
                match=False

            if key=="age_max" and user["age"]>value:
                match=False

            if key=="gender" and user["gender"]!=value:
                match=False

            if key=="caste" and user["caste"]!=value:
                match=False

            if key=="area" and user["area"]!=value:
                match=False

            if key=="marital_status" and user["marital_status"]!=value:
                match=False

            if key=="has_house" and user["has_house"]!=value:
                match=False

            if key=="is_farmer" and user["is_farmer"]!=value:
                match=False

            if key=="land_max" and user["land"]>value:
                match=False

            if key=="is_student" and user["is_student"]!=value:
                match=False

            if key=="disability" and user["disability"]!=value:
                match=False

        if match:
            eligible.append(scheme)

    return eligible