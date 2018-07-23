# from sequence having each item as a pair
my_dict = {}
my_dict = {1:'apple',2:'ball',3:'cat'} # dictionary
my_dict = {"Name": "Ramya", 1: [1,2,3,4]} # mixed keys
my_dict = dict({1:'apple', 2:'ball'}) #Tuple to dict
my_dict = dict([(1,'apple'), (2,'ball')]) #list of  2 tuples ->tuple -> dict 
my_dict = {'name':'Jack', 'age': 26}
print my_dict["name"]
print my_dict.get("age")
my_dict["age"] = 27
my_dict["address"] = "Delhi" #adding
print my_dict

