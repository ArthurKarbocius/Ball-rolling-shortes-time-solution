# # # <<<<<<<<<<<< ball rolling total time solution of fucntion x^k + y^k = h^k >>>>>>>>>>>>>>>>>
import math
# Total iteration number:
N = 10**5
# Function's power coefficient in range k=(0, 1]:
k = 1/2
# Defining (max.) distance at x-axis, [m]:
x0 = 1
# Max. altitude at y-axis, [m]:
h = x0 
# Free fall accelaration constant, [m/s^2]:
g = 9.81
# Maximum ball rolling velocity [m/s]:
v0 = (2*g*h)**(1/2)
# Initial length, velocity and time:
Sn_sum = 0
vn = v0
tn_sum = 0
  
for n in range(N):  
        # Coordinates of xn and yn:
        xn = x0*(1 - n/N)
        yn = (h**k - xn**k)**(1/k)
        # Coordinates of xn+1 and yn+1:
        x2 = x0*(1 - (n + 1)/N)
        y2 = (h**k - x2**k)**(1/k)
        # Curve segments Sn lengths:
        Sn = ((y2 - yn)**2 + (xn - x2)**2)**(1/2)
        # Total function's yn curve length:
        Sn_sum += Sn
        # Curve slope angles in degree units:
        angle_n = math.atan((y2 - yn)/(xn - x2))*180/math.pi
        # At every curve segment Sn and at every angle_n ball velocity: 
        vn = vn - g*Sn/vn*math.sin(angle_n*math.pi/180)
        # Ball roll times tn at every curve length segment Sn: 
        tn = Sn/vn
        # Total ball roll time over entire curve length Sn_sum:
        tn_sum += tn

if tn_sum == tn_sum:
        print("Total time =",tn_sum,"seconds")
        print("Total curve's length =",Sn_sum,"meters")



# # <<<<<<<<<<<< Optimization algorithm to find curve k power coefficient {min_k = k} which satisfy minimum rolling time t = {min_tn_sum} condition >>>>>>>>>>>>>>>>>

# import math

# N = 10**5
# x0 = 1
# h = x0
# g = 9.81
# v0 = (2*g*h)**(1/2)
# # minimum time t_min=0.451523641 seconds when ball roll (fall) perpendicular to the ground:
# t_min = (2*h/g)**(1/2) 

# k_min = 0.69 # minimum value of k
# k_max = 0.71 # maximum value of k
# k_step = 0.0001 # step size for k
# min_tn_sum = float('inf') # set initial value to infinity

# for k in range(int(k_min/k_step), int(k_max/k_step)): # iterate over range of k values
#     k = k * k_step # convert k back to its actual value
#     Sn_sum = 0
#     tn_sum = 0
#     vn = v0
    
#     for n in range(N):
#         xn = x0*(1 - n/N)
#         yn = (h**k - xn**k)**(1/k)
#         x2 = x0*(1 - (n + 1)/N)
#         y2 = (h**k - x2**k)**(1/k)
#         Sn = ((y2 - yn)**2 + (xn - x2)**2)**(1/2)      
#         angle_n = math.atan((y2 - yn)/(xn - x2))*180/math.pi       
#         vn = vn - g*Sn/vn*math.sin(angle_n*math.pi/180)
#         tn = Sn/vn
#         tn_sum += tn
#     if tn_sum < min_tn_sum:
#         min_tn_sum = tn_sum
#         min_k = k

# print(f"Minimum value of tn_sum is {min_tn_sum} at k = {min_k}")

# # ===================== Result for max iterations N = 10**8 is k = 0.7005 ===============================

    
