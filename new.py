with open('normaltext.txt', 'r') as file:
    
    line_count = 0
    
   
    for line in file:
       
        line_count += 1
        
     
        print(line_count,line.strip())