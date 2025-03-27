def sum_odd_and_even(lst):
    return [sum(e for e in lst if e%2==i) for i in [0,1]]

print(sum_odd_and_even([1,3,5,76,45,3,7856,4]))
print([sum(a for a in [0,1] if not a==0) for j in [1,2]])

PI = 3.14
PI = 3.15
print(PI)

a_b_c = 1,000,000
print(a_b_c)
