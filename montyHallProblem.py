import random
import copy
import threading

params_o = {
    "iteration-count": 10000000,
    "door-count": 3,
    "door-map": [],
    "wrong-index-map": [],
    "correct-index": 0,
    "pick": 0,
    "possible-doors-to-open": [],
    "open-doors": [],
    "other-closed-door-index": 0,
    "stayed-door": 0,
    "other-door": 0,
    "prob_fc": 0,
    "prob_od": 0
}

def generate_door_map(params):
    for i in range(params["door-count"]-1): params["door-map"].append("lose"+str(i))
    params["door-map"].append("win")
    random.shuffle(params["door-map"])
    for door in params["door-map"]:
        if "lose" in door: params["wrong-index-map"].append(params["door-map"].index(door))
        if "win" in door: params["correct-index"] = params["door-map"].index(door)
    return params

def choose(params):
    params["pick"] = random.randint(0, params["door-count"]-1)
    return params

def open_other_doors(params):
    possible_doors_to_open = copy.copy(params["wrong-index-map"])
    if params["pick"] in possible_doors_to_open: possible_doors_to_open.remove(params["pick"])
    params["possible-doors-to-open"] = copy.copy(possible_doors_to_open)
    for i in range(0, params["door-count"]-2):
        choice = random.choice(possible_doors_to_open)
        params["open-doors"].append(choice)
        possible_doors_to_open.remove(choice)
    return params

def get_other_closed_door(params):
    for door_index in [i for i in range(0, params["door-count"])]:
        if door_index not in params["open-doors"] and door_index != params["pick"]: params["other-closed-door-index"] = door_index
    return params

def evaluate_turn(params):
    if params["door-map"][params["pick"]] == "win": params_o["stayed-door"] += 1
    elif params["door-map"][params["other-closed-door-index"]] == "win": params_o["other-door"] += 1
    else: print("error")

def run(params):
    params = generate_door_map(params)
    params = choose(params)
    params = open_other_doors(params)
    params = get_other_closed_door(params)
    evaluate_turn(params)

def evaluate_end_results():
    params_o["prob_fc"] = params_o["stayed-door"] / params_o["iteration-count"] * 100
    params_o["prob_od"] = params_o["other-door"] / params_o["iteration-count"] * 100
    print(f'First choice: {params_o["stayed-door"]}, other door: {params_o["other-door"]}')
    print(f'First choice: {params_o["prob_fc"]}%, other door: {params_o["prob_od"]}%')

if __name__ == "__main__":
    for i in range(0, params_o["iteration-count"]-1):
        params_n = copy.deepcopy(params_o)
        thread = threading.Thread(target=run, args=(params_n,))
        thread.run()
    evaluate_end_results()