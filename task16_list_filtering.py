# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# It's from practice and repeat. I've also solved few bags on codewars directly.
def filter_list(l):
    return [elem for elem in l if isinstance(elem, int)]
print(filter_list([1,2,'a','b']))
