"""Tiny turtle simulator used to verify every code-tracing answer in the unit tests.

Program strings: F=forward, L=left, R=right with a number; U=penup, D=pendown.
run(P("F100 R90 F50")) -> (final position, final heading, drawn segments, stamps)
"""
import math
def run(prog):
    x=y=0.0;h=0;pen=True;col="black";size=1;segs=[];stamps=[]
    for c,*a in prog:
        if c=="F":
            nx=x+a[0]*math.cos(math.radians(h));ny=y+a[0]*math.sin(math.radians(h))
            if pen: segs.append(((round(x),round(y)),(round(nx),round(ny)),col,size))
            x,y=nx,ny
        elif c=="L":h=(h+a[0])%360
        elif c=="R":h=(h-a[0])%360
        elif c=="U":pen=False
        elif c=="D":pen=True
        elif c=="C":col=a[0]
        elif c=="S":size=a[0]
        elif c=="ST":stamps.append((round(x),round(y)))
    names={0:"right",90:"up",180:"left",270:"down"}
    return (round(x),round(y)),names.get(round(h)%360,h),segs,stamps
P=lambda s:[(t[0],int(t[1:])) if t[0] in"FLR" else (t,) for t in s.split()]


if __name__ == "__main__":
    print(run(P("F100 L120 F100 L120 F100 L120"))[:2])  # triangle: back at start, facing right
