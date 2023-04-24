# Generalized Lucas Theorem to find nCm mod p^q 
def comb_lucas(n, m, p, q):
    r = n-m
    mod = pow(p, q)
    temp_n, temp_m, temp_r = n,m,r
    base_p_nmr = [] # list of tuples: (n_i, m_i, r_i), where n_i represents the ith digit of 'n' in base p.
    i, e0, eq = 0, 0, 0 # eq: number of digits in base p on or after the 'q-1'th digit where n_i < m_i  
    while temp_n > 0 or temp_m > 0 or temp_r > 0:
        temp_n, n_i = divmod(temp_n, p)
        temp_m, m_i = divmod(temp_m, p)
        temp_r, r_i = divmod(temp_r, p)
        base_p_nmr.append( (n_i, m_i, r_i) )
        if n_i < m_i:
            e0 += 1
            if i >= q-1:
                eq += 1
        i += 1

    if p == 2 and q >= 3: t1 = 1 # first term in equation (3), with the (+/- 1)
    else: t1 = -1
    t1 = pow(p, e0) * pow(t1, eq)
     
    # list of tuples: (N_i, M_i, R_i)
    NMR = [ (n//p**j % mod, m//p**j % mod, r//p**j % mod) for j in range(len(base_p_nmr)) ]

    modified_factorials = [1] # pre-compute modified factorials. Modified factorial(x) is the product of all integers <= x that are not divisible by p 
    for i in range(1, max(max(NMR)) + 1):
        if (i % p == 0): modified_factorials.append(modified_factorials[i-1]) # Modified factorials do not include integers divisible by p
        else: modified_factorials.append( modified_factorials[i-1] * i % mod )

    ans = t1 # we start with the first term in the product and multiply for each digit in base p.
    for N_i, M_i, R_i in NMR:
        ans = ans * modified_factorials[N_i] * pow(modified_factorials[R_i] * modified_factorials[M_i], -1, mod) % mod
    return ans