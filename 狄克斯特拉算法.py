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
  lowest_cost = float("inf") 
  lowest_cost_node = None
  for node in costs: 
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost 
      lowest_cost_node = node 
  return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  print cost
