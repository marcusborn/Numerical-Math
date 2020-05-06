#Heron's Method for calculating square roots.

#xi = 1/2 * (xn + a/xn) #xi=initial guess, xn = iterations
def heron(xi, a, its=10):# a is the number we want to root.
     for i in range(0, its):
          xnew = 1/2 * (xi + a/xi)
          xi = xnew
          print(str(xi) + "with " + str(i) + " iterations")
     return xnew

