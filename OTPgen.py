#import library 
import math, random 

# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    
    num = "0123456789"
    OTP=" "

   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += num[math.floor(random.random() * 10)] 
  
    return OTP 
# Driver code 
if __name__ == "__main__" : 
      
    print("OTP of 4 digits:",generateOTP()) 
