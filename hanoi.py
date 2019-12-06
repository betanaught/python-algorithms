def move(f, t):
    print("Move disk from {} to {}".format(f, t))

def moveVia(f, v, t) :
    move(f, v)
    move(v, t)

def foo(x) :
    foo(x)

def hanoi(n, f, h, t) : # disks, from, helper, target
    if n==0 :
        pass
    else :
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)

hanoi(5, 'a', 'b', 'c')
