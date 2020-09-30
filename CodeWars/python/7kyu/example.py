def to_upper_case(s):
    

    
    return str(s).upper()
    

# map_iterator = map(to_upper_case, "abc")
# print(type(map_iterator))
# print(map_iterator)
print(to_upper_case("s"))
map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_list = list(map_iterator)
print(my_list)
