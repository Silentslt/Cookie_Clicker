import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
save_file = os.path.join(dir, "playerdata.json")

levels = ["CRUMB","BITE","JUMBO COOKIE","ELON CRUMB","COOKIE BANK"]


upgrade_cost = {
    "CRUMB": 10,
    "BITE": 50,
    "JUMBO COOKIE": 150,
    "ELON CRUMB": 500,
    "COOKIE BANK": None
}


click_Value = {
    "CRUMB": 1,
    "BITE": 2,
    "JUMBO COOKIE": 5,
    "ELON CRUMB": 10,
    "COOKIE BANK": 20
}


default_data = {
    "Level": levels[0],
    "total_score": 0,

}


def load_data():
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            data = json.load(file)
            return data
    else: 
        return default_data 

def save_data(data):
    try:
        os.makedirs(dir, exist_ok=True)
        with open(save_file, "w") as file:
            json.dump(data, file, indent=4)
    except OSError as e:
        return

def get_click_value(data):
    return click_Value[data["Level"]]


    
def update_score(data,amount):
    data["total_score"] += amount
    save_data(data)


def get_upgrade_cost(data):
    return upgrade_cost[data["Level"]]



def can_upgrade(data):
    cost = get_upgrade_cost(data)
    if cost is None:
        return False
    return data["total_score"] >= cost

def update_level(data, new_level):
    data["Level"] = new_level
    save_data(data)


def next_level(data):
    cost = get_upgrade_cost(data)
    if cost is None:
        return False  
    if data["total_score"] < cost:
        return False 

    data["total_score"] -= cost
    current_index = levels.index(data["Level"])
    data["Level"] = levels[current_index + 1]
    save_data(data)
    return True