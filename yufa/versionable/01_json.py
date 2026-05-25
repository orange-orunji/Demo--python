"""
    JSOn数据格式转换
"""
import json
# data_map = {
#     "name": "Bob",
#     "languages": ["English", "French"]
# }
data_map=[{"name": "Bob", "languages": ["English", "French"]}]
dumps = json.dumps(data_map)
print(dumps)
print(type(dumps))
loads = json.loads(dumps)
print( loads)
print(type(loads))