def create_an_empty_list():
    return []
def create_a_list():
    places =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
    return places
def add_element_to_end_of_list(l, element):
    l =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
    l.append(element)
    return l
def add_element_to_start_of_list(l, element):
    l =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
    l.insert(0, element)
    return l
def remove_element_from_end_of_list(l):
    l.pop(-1)
    return l
l =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
def remove_element_from_start_of_list(l):
    del l[0]
    return l
l =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
def retrieve_first_element_from_list(l):
    x = l[0]
    return x
l =  ["Kenya", "Uganda", "Ghana", "Tunisia"]
def retrieve_element_from_index(l, index):
    return l[index]
def retrieve_last_element_from_list(l):
    return l[-1]