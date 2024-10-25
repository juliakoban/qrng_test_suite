import math
import scipy.special as ss

# The focus of this test is the length of a linear feedback shift register (LFSR). The purpose of this test is to
# determine whether or not the sequence is complex enough to be considered random. Random sequences
# are characterized by longer LFSRs. An LFSR that is too short implies non-randomness. 

BLOCK_LENGHT = 500
DEGREES_OF_FREEDOM = 6

def padding( input, n ):
    return "0" * ( n - len( input ) ) + input

def berlekam_massey( input ):
    n = len(input)

    b = "1" + "0" * (n - 1)
    c = "1" + "0" * (n - 1)

    L = 0
    m = -1
    N = 0
    
    while N < n:
        d = int( input[N], 2 )  
        
        if L > 0:
            k = int( c[1:L + 1], 2 ) 
            h = int( input[N - L:N][::-1], 2 )  
            r = bin( k & h ).count( "1" )  
            d ^= ( r % 2 ) 

        if d != 0:
            t = c
            k = int( c[N - m:], 2 )
            h = int( b[:n - N + m], 2 )
            c = c[:N - m] + padding( bin( k ^ h )[2:], n - N + m )
            
            if L <= N // 2:
                L = N + 1 - L
                m = N
                b = t  
        N += 1
    return L, c[:L]

def linear_complexity_test( input, M = BLOCK_LENGHT, K = DEGREES_OF_FREEDOM ):
    n = len( input )
    if n < 10**6:
        return 0
    N = math.floor( n / M )
    miu = ( M / 2. ) + ( ( 9 + ( -1 )**( M + 1 ) ) / 36. ) - ( ( ( M / 3. ) + ( 2. / 9. ) ) / 2**M )
    T = list( )
    for i in range( N ):
        block = input[i * M:( i + 1 ) * M]
        lc =  berlekam_massey( block )[0] 
        T.append( ( ( -1 )**M * ( lc - miu ) ) + ( 2. / 9. ) )
        
    v = [0, 0, 0, 0, 0, 0, 0]
    for value in T:
        if value <= -2.5: v[0] += 1
        elif value > -2.5 and value <= -1.5: v[1] += 1
        elif value > -1.5 and value <= -0.5: v[2] += 1
        elif value > -0.5 and value <= 0.5: v[3] += 1
        elif value > 0.5 and value <= 1.5: v[4] += 1
        elif value > 1.5 and value <= 2.5: v[5] += 1
        else: v[6] += 1
      
    pi = [0.01047, 0.03125, 0.12500, 0.50000, 0.25000, 0.06250, 0.020833]
    chi_squared = 0.0 
    for i in range( K + 1 ):
        chi_squared += ( ( v[i] - ( N * pi[i] ) )**2 / ( N * pi[i] ) )
    p_value = ss.gammaincc(  ( K / 2.0 ), ( chi_squared / 2.0 ) ) 
    return p_value