def divCount(n):
 
    hh = [1] * (n + 1);
      
    p = 2;
    while((p * p) < n):
        if (hh[p] == 1):
            for i in range((p * 2), n, p):
                hh[i] = 0;
        p += 1;

    total = 1;
    for p in range(2, n + 1):
        if (hh[p] == 1):
  
            count = 0;
            if (n % p == 0):
                while (n % p == 0):
                    n = int(n / p);
                    count += 1;
                total *= (count + 1);
                  
    return total;
  


J = int(input())
if(J<=0):
    print("Please provide a valid positive integer")
else:    
    count = 0
    for i in range(1,J+1):
        val=divCount(i)
        
        if(val>3):
            count=count+1;
    print(count)