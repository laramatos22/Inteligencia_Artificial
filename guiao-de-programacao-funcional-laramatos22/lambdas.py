sum_two_numbers = lambda a, b : a+b

print("sum_two_numbers(2, 3) = ", sum_two_numbers(2, 3))

lst = (("Rafael", 10), ("John", 11), ("May", 12))
sorted_lst = sorted(lst, lambda t : t[1])
print(sorted_lst)

def xpto(f, h, v1, v2, v3, v4):
    return f(h(v1, v2, v3, v4))

print(xpto(lambda a, b: a+b, lambda a,b : a*b, 1, 2, 3, 4))

# f( g(v1, v2), g(v3, v4) )
# f( 2*1, 3*4 )
# f( 2, 12 )

