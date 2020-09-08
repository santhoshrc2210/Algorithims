'''product of two numbers using recursive multiplication'''
def recursive_mult(a,b):
   
    if len(str(a))==1:
        return a*b
    else:
        a_str=str(a)
        b_str=str(b)
        
        if len(a_str)%2!=0:
            a_str='0'+a_str
        if len(b_str)%2!=0:
            b_str='0'+b_str 
        l_a=len(a_str)
        l_b=len(b_str)  
        
        a_half=int(a_str[:l_a/2])
        b_half=int(a_str[l_a/2:])
        c_half=int(b_str[:l_b/2])
        d_half=int(b_str[l_b/2:])
        
        sol=(10**l_a)*recursive_mult(a_half,c_half)
        sol2=(10**(l_a/2))*(recursive_mult(a_half,d_half)+recursive_mult(b_half,c_half))
        return sol+sol2+recursive_mult(b_half,d_half)

num1=3141592653589793238462643383279502884197169399375105820974944592
num2=2718281828459045235360287471352662497757247093699959574966967627    
prod=recursive_mult(num1,num2)
print prod
