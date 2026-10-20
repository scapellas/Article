# Cylindrical coordinates, with Br = 0, and Btheta, Bz depending only on r. This guarantees div(B) = 0.
# q and zeta are adimensional parameters for the magnetic field profile.
# For zeta = 1, we obtain the Force-Free Gold-Hoyle model.
# B0 is the max magnetic field, expressed in Teslas.
# r is the normalized distance to the axis (divided by R).

B0 = 1

def Bz(r, q, zeta):
    return B0/(1+(q*r)**2)

def Btheta(r, q, zeta):
    return q*(r**zeta)*Bz(r, q, zeta)

def dBz(r, q, zeta):
    return -(2*q**2*r)/(q**2*r**2 + 1)**2

def dBtheta(r, q, zeta):
    return (zeta*q*r**(zeta - 1))/(q**2*r**2 + 1) - (2*q**3*r**(zeta + 1))/(q**2*r**2 + 1)**2