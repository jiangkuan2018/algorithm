#coding=utf-8
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()
best_station = None
states_covered = set()

# set1 = set(['eli','xiangjiao','xihongshi'])
# set2 = set(['tiancai','huluobo','xihongshi'])
# print set1 | set2

for station, states_for_station in stations.items():
  #station是key
  #states_for_station是值
  # print station, states_for_station
  covered = states_needed & states_for_station
  if (len(covered) > len(states_covered)):
    print covered
    best_station = station
    states_covered = covered

print best_station