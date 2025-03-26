def sort_dict(lst,key): #sort a list if dict by a key
    return sorted(lst,key=lambda x:x[key])

people = [{"name":'Alice', "age":30},{"name":'lagartha', "age":27},{"name":'Ragnar', "age":33},]
print(sort_dict(people,"age"))