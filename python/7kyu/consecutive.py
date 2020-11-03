def cons_items(arr, a, b):
    if a in arr and b in arr:
        return True
    else:
        return False 


# The function checks if the array elements  
# are consecutive. If elements are consecutive,  
# then returns true, else returns false  
def areConsecutive(arr, n): 
  
    if ( n < 1 ): 
        return False
      
    # 1) Get the Minimum element in array */ 
    Min = min(arr) 
      
    # 2) Get the Maximum element in array */ 
    Max = max(arr) 
      
    # 3) Max - Min + 1 is equal to n,  
    # then only check all elements */ 
    if (Max - Min + 1 == n): 
          
        # Create a temp array to hold visited  
        # flag of all elements. Note that, calloc  
        # is used here so that all values are  
        # initialized as false 
        visited = [False for i in range(n)] 
      
        for i in range(n): 
              
            # If we see an element again,  
            # then return false */ 
            if (visited[arr[i] - Min] != False): 
                return False
      
            # If visited first time, then mark 
            # the element as visited */ 
            visited[arr[i] - Min] = True
      
        # If all elements occur once, 
        # then return true */ 
        return True
      
    return False # if (Max - Min + 1 != n) 



if __name__ == "__main__":
    print(cons_items([1,2,3], 1, 2))