import math


def print_matrix( matrix ):
    retStr = ""
    for c in range( len( matrix ) ):
        retStr += "["
        for r in range( len( matrix[c] ) ):
            if ( r == len( matrix [c] ) - 1):
                retStr += str( matrix[c][r] ) + "]\n"
            else:
                retStr += str( matrix[c][r] ) + ", "
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
    for c3 in range ( len ( m2[0] ) ):
        m3.append( [] )
        for r3 in range ( len ( m2 ) ):
            m3[c3].append( m2[r3][c3] )
    print_matrix (m3)

    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( c*r+r )
    return m
m = new_matrix()
l = new_matrix()
print_matrix(m)
scalar_mult(m,5)
print_matrix(m)
matrix_mult(l,m)
