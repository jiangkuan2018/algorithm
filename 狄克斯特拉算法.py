# coding=utf-8
graph = {} # 图
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {} # 开销表
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}  # 储存节点的父节点
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] # 以处理过的节点

def find_lowest_cost_node(costs):
  lowest_costs = float('inf')
  lowest_costs_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_costs and node not in processed:
      lowest_costs = cost # 花销
      lowest_costs_node = node # 节点
  return lowest_costs_node

node = find_lowest_cost_node(costs)

while node is not None:
  cost = costs[node] # 当前最小花销
  neighbors = graph[node] # 找到最小花销节点的下一级
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
  processed.append(node)
  node = find_lowest_cost_node(costs)
  print(node)
