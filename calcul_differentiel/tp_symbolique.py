"""Complément facultatif des TP : python tp_symbolique.py (SymPy requis)."""
import sympy as sp


def symbolic_results():
    rho,theta,phi,z=sp.symbols('rho theta phi z',real=True)
    spherical=sp.Matrix([rho*sp.cos(theta)*sp.sin(phi),rho*sp.sin(theta)*sp.sin(phi),rho*sp.cos(phi)])
    cylindrical=sp.Matrix([rho*sp.cos(theta),rho*sp.sin(theta),z])
    x,y=sp.symbols('x y',real=True)
    cubic=x**3+y**3-3*x*x*y-3*x*x
    t=sp.symbols('t',real=True)
    a,b,c,d=sp.symbols('a b c d',real=True)
    h11,h12,h21,h22=sp.symbols('h11 h12 h21 h22',real=True)
    A=sp.Matrix([[a,b],[c,d]]);H=sp.Matrix([[h11,h12],[h21,h22]])
    return {
        'Jacobienne sphérique (rho, theta, phi)':sp.simplify(spherical.jacobian([rho,theta,phi])),
        'Déterminant sphérique signé':sp.trigsimp(spherical.jacobian([rho,theta,phi]).det()),
        'Jacobienne cylindrique':cylindrical.jacobian([rho,theta,z]),
        'Déterminant cylindrique':sp.trigsimp(cylindrical.jacobian([rho,theta,z]).det()),
        'Gradient du polynôme':sp.Matrix([sp.diff(cubic,x),sp.diff(cubic,y)]),
        'Hessienne du polynôme':sp.hessian(cubic,[x,y]),
        'Points critiques':sp.solve([sp.diff(cubic,x),sp.diff(cubic,y)],[x,y]),
        'D det(A)[H]':sp.diff((A+t*H).det(),t).subs(t,0),
        'D inverse(A)[H], sur GL2':sp.simplify(-A.inv()*H*A.inv()),
    }


if __name__=='__main__':
    for title,value in symbolic_results().items():
        print('\n'+title);sp.pprint(value,use_unicode=True)
