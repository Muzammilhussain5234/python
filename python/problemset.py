# problem1
class twodvector:
    def __init__(s,i,j):
        s.i = i
        s.j = j
    def show(s,i,j):
        print(f"Vector  is ({s.i}i, {s.j}j)")
class threevector(twodvector):
    def __init__(s,i,j,k):
        super().__init__(i,j)   
        s.k = k
    def show(s,i,j,k):
        print(f"Vector is ({s.i}i, {s.j}j, {s.k}k)")   
v= threevector(2,3,4)
v.show(2,3,4)    
t= twodvector(2,3)
t.show(2,3)      
    