

import json
#
# d = dict(name='bob',age=20,score=90)
# print(json.dumps(d))

# json_str='{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))
s = Student('fa',23,90)
print(json.dumps(s,default=lambda obj:obj.__dict__))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)


