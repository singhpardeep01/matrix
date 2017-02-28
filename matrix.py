import math


def print_matrix( matrix ):
    retStr = ""
    for c in range( len( matrix ) ):
        for r in range( len( matrix[c] ) ):
            if ( r == len( matrix [c] ) - 1):
                retStr += str( matrix[c][r] ) + "\n"
            else:
                retStr += str( matrix[c][r] ) + " "
    print(retStr)
    pass

def ident( matrix ):
    for c in range( len( matrix ) ):
        for r in range( len( matrix[c] ) ):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    pass

def scalar_mult( matrix, s ):
    for c in range( len( matrix ) ):
        for r in range( len( matrix[c] ) ):
            matrix[c][r] = matrix[c][r] * s
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = []
    for c3 in range ( len ( m1[0] ) ):
        m3.append( [] )
        for r3 in range ( len ( m1 ) ):
            m3[c3].append( m1[r3][c3] )
    m4 = m2
    for c2 in range ( len( m2 ) ):
        for r2 in range ( len ( m2[c2] ) ):
            m2[c2][r2] = m1[0][r2]*m4[0][r2] + m1[1][r2]*m4[1][r2] + m1[2][r2]*m4[2][r2] + m1[3][r2]*m4[3][r2]   
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 + r)
    return m
"""
m = new_matrix()
l = new_matrix()
ident(l)
scalar_mult(l,5)
print "m\n"
print_matrix(m)
print "l\n"
print_matrix(l)
matrix_mult(l,m)
print "m\n"
print_matrix(m)
print "l\n"
print_matrix(l)
"""
