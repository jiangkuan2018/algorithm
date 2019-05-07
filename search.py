# code=utf-8
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
  search_queue = deque() #  创建队列
  search_queue += graph[name] # 添加被检查者的所有一度关系
  searched = []  # 记录被检查过的元素
  path = []
  while search_queue: # 如果队列不为空一直检查
    person = search_queue.popleft()  # 取出队列的第一项 FO
    path.append(person)
    if not person in searched:  # 如果检查者没有被检查过
      if person_is_seller(person):  # 如果检查者是seller 返回true
        path.insert(0, name)
        print(person + ' is seller' , path)
        return True
      else:
        path = []
        search_queue += graph[person] # 如果检查者不是seller 添加检查者的所有一度关系
        searched.append(person)  # 将被检查者记录到数组中
  print 'not found seller'
  return False # 如果都没有 返回false

def person_is_seller(name): # 条件
  return name[-1] == 'm'

search('you')