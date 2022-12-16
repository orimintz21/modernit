import number_theory_functions
"""N = 12215009
e = 3499
q = 3491
p = 3499
K = (p - 1) * (q - 1)
MM = 42
d = number_theory_functions.modular_inverse(e, K)
M = number_theory_functions.modular_exponent(MM, d, N)
print(K)
print(d)
print(M)
"""
a = 911
b = 7879
c = 1000000
(d, x, y) = number_theory_functions.extended_gcd(a, b)
print(d)
print(x*c)
print(-y*c)
