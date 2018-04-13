# (C) 2017 University of Bristol. See License.txt
#Based on "Algorithm 173 SQL Query"

#-----------------------------------------------------------------------------#
L = (20, 20, 20, 20, 20, 83, 20, 2, 10, 50)
a = 5              # 5 <= a <= 14
v = 0              # 0 <= v <= 4
N = 1000

#-----------------------------------------------------------------------------#
def read_row():
    sInteger_0 = sint.get_input_from(0)
    sInteger_1 = sint.get_input_from(0)
    sInteger_2 = sint.get_input_from(0)
    sInteger_3 = sint.get_input_from(0)
    sInteger_4 = sint.get_input_from(0)
    
    s20BitArray_5 = Array(L[0], sint)
    for i in range(L[0]):
        s20BitArray_5[i] = sint.get_input_from(0)
    
    s20BitArray_6 = Array(L[1], sint)
    for i in range(L[1]):
        s20BitArray_6[i] = sint.get_input_from(0)
    
    s20BitArray_7 = Array(L[2], sint)
    for i in range(L[2]):
        s20BitArray_7[i] = sint.get_input_from(0)
    
    s20BitArray_8 = Array(L[3], sint)
    for i in range(L[3]):
        s20BitArray_8[i] = sint.get_input_from(0)
    
    s20BitArray_9 = Array(L[4], sint)
    for i in range(L[4]):
        s20BitArray_9[i] = sint.get_input_from(0)
    
    s83BitArray_10 = Array(L[5], sint)
    for i in range(L[5]):
        s83BitArray_10[i] = sint.get_input_from(0)
    
    s20BitArray_11 = Array(L[6], sint)
    for i in range(L[6]):
        s20BitArray_11[i] = sint.get_input_from(0)
    
    s2BitArray_12 = Array(L[7], sint)
    for i in range(L[7]):
        s2BitArray_12[i] = sint.get_input_from(0)
    
    s10BitArray_13 = Array(L[8], sint)
    for i in range(L[8]):
        s10BitArray_13[i] = sint.get_input_from(0)
    
    s50BitArray_14 = Array(L[9], sint)
    for i in range(L[9]):
        s50BitArray_14[i] = sint.get_input_from(0)

    return (sInteger_0, sInteger_1, sInteger_2, sInteger_3, sInteger_4, s20BitArray_5, s20BitArray_6, s20BitArray_7, s20BitArray_8,
            s20BitArray_9, s83BitArray_10, s20BitArray_11, s2BitArray_12, s10BitArray_13, s50BitArray_14)

#-----------------------------------------------------------------------------#
def print_tup(t):
    print_ln('showing 5 integers')
    for i in range(5):
        print_ln('int %s = %s', i, t[i].reveal())

    for i in range(5, 15):
        print_ln('showing bit array %s', i)
        for j in range(L[i-5]):
            print_ln('bit %s = %s', j, t[i][j].reveal())

#-----------------------------------------------------------------------------#

S = Array(L[a], sint)
C = Array(L[a], sint)

@for_range(N)
def perform_row(i):
    Ti = read_row()
    #print_tup(Ti)
    for j in range(L[a-5]):
        S[j] = S[j] + Ti[v]*Ti[a][j]
        C[j] = C[j] + Ti[a][j]

R = Array(L[a-5], sfix)
for j in range(L[a-5]):
    sfSj = sfix(0)
    sfSj.load_int(S[j])
    sfCj = sfix(0)
    sfCj.load_int(C[j])
    R[j] =sfSj/sfCj
    print_ln('R[%s] = %s; C[%s] = %s;', j, R[j].reveal(), j, C[j].reveal())

#-----------------------------------------------------------------------------#
print_ln('Algorithm 173 SQL Query test done')
