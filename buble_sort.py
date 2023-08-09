
def buble_sort(variable):
    try:
        variable=list(variable)
    except: "Cannot be converted into list"
    temp=variable
    try:
        if len(variable)==0:
            return None
    
        elif len(variable)==1:
            return(temp)
        
        else:
            for x in variable:
                flag=False
                cycle=len(variable)-1
                for _i, _var in enumerate(temp):
                    if _i==cycle:
                        None
                    else: 
                        if(_var > temp[_i+1]):
                            temp[_i]=temp[_i+1]
                            temp[_i+1]=_var
                            flag=True
                cycle-=1
                if flag==False:
                    break
            return(temp)
    except:print("Only list allowed")
    

argument1=None
argument2=[1,2,5,3,1,7,9,1,12,83,1,5,3,2]
argument3=(1,1,1,1,1,1,1,2,1,1,1)
argument4=(2,2,2,2)
argument5=(1,2)
argument6=(2,1)

print(buble_sort(argument1))
print(buble_sort(argument2))
print(buble_sort(argument3))
print(buble_sort(argument4))
print(buble_sort(argument5))
print(buble_sort(argument6))
                    