import math
h = [[2, 6], [2, 5], [8, 4]]
t = [7, 2, 3]

adv_h = [(2+2+8)/3, (6+5+4)/3]

adv_t = (7+2+3)/3

for k in range(2):
    est1 = 0
    est2 = 0
    est3 = 0
    for d in range(len(h)):
        est1 += (h[d][k]-adv_h[k])*(t[d]-adv_t)
        est2 += (h[d][k]-adv_h[k])**2
        est3 += (t[d]-adv_t)**2
    print(est1/math.sqrt(est2*est3))
