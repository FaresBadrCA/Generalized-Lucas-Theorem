# Generalized Lucas Theorem to find nCm mod p^q 
def comb_lucas(n, m, p, q):
    r = n-m
    mod = pow(p, q)
    d = 0 # number of digits in base p
    e0, eq = 0, 0 # eq: number of digits in base p on or after the 'q-1'th digit where n_i < m_i  
    temp_n, temp_m = n,m
    while temp_n > 0 or temp_m > 0:
        temp_n, n_i = divmod(temp_n, p)
        temp_m, m_i = divmod(temp_m, p)
        if n_i < m_i:
            e0 += 1
            if d >= q-1:
                eq += 1
        d += 1

    if p == 2 and q >= 3: t1 = 1 # first term in equation (3), with the (+/- 1)
    else: t1 = -1
    t1 = pow(p, e0) * pow(t1, eq)
     
    NMR = [ (n//p**j % mod, m//p**j % mod, r//p**j % mod) for j in range(d) ] # list of tuples: (N_i, M_i, R_i)

    modified_factorials = [1] # pre-compute modified factorials. (x!)_p is the product of all integers <= x that are not divisible by p 
    for i in range(1, max(max(NMR)) + 1):
        if (i % p == 0): modified_factorials.append(modified_factorials[i-1])
        else: modified_factorials.append( modified_factorials[i-1] * i % mod )

    ans = t1 # we start with the first term in the product and multiply for each digit in base p.
    for N_i, M_i, R_i in NMR:
        ans = ans * modified_factorials[N_i] * pow(modified_factorials[R_i] * modified_factorials[M_i], -1, mod) % mod
    return ans