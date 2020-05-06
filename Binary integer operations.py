#convert to binary ONLY WORKS FOR INTEGERS

def binary(num):
     powers = list(range(15,-1,-1))
     nums_in_powers = []
     for i in powers:
          
          if 2**i <= num:
               nums_in_powers.append(str(1))
               num = num - 2**i
          else:
               nums_in_powers.append(str(0))
     bin_nums = "".join(nums_in_powers)
     bin_nums_stripped = bin_nums.lstrip("0")
     return bin_nums_stripped
     print(bin_nums_stripped)
     
     
#convert to decimal

def dec(num):
     powers = list(range(len(str(num))-1,-1,-1))#needs to be a backwards list
     decimal = 0
     for i in powers:

          if str(num)[i] == str(1):
               decimal += 2**powers[i]
     return decimal
     print(decimal)
                   
#binary multiplication

def bin_prod(num1, num2):
     dec_ans = dec(num1)*dec(num2) #answer in decimal
     ###big problem here with converting to decimal
     print(dec_ans)
     bin_ans = binary(dec_ans)
     #return bin_ans
     print(bin_ans)

#####only for integers  
def bin_div(num1, num2):
     dec_ans = dec(num1)/dec(num2) #answer in decimal
     bin_ans = binary(dec_ans)
     #return bin_ans
     print(bin_ans)
