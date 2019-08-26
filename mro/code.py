class A(object): pass
class B(object): pass
class X(A, B): pass
class Y(A, B): pass
# class Y(B, A): pass    # inconsistent MRO for base classes A & B
class Z(X, Y): pass


print(Z.mro())
