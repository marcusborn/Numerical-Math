#Euclidian algorithm

#Find Greatest common denominator- the largest number that divides two numbers evenly

#This needs to be an arbitrary no. != 0


#ditch the number on rhs, shift everything right

#denom = numer*q + r #q is quotient, r is remainder
def euclid(numer,denom):
     r =1
     while r != 0:
          rfinal = r
          q = numer//denom #use integer devision to get the factor
          r = numer - q*denom
          print("{0} = {1}*{2} + {3}".format(numer, denom, q, r)) 
          numer = denom
          denom = r
     print("the greatest common denomenator is %d" %rfinal)
