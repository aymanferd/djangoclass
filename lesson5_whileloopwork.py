'''
While loop
____________
init variable
while <condition>:
    statements
    ...
'''
start=int(input("Enter the start value: "))

stop=int(input("Enter the stop value: "))
i=start
while i<=stop:
    if i%2!=0:
        print(i ,end="\t")
    
    #i=i+1
    i+=1
    
    
    #compound assignment operator
    