
def buble_sort(variable):
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
    except:print("Only list")
    

argument=[1,2,5,3,1,7,9,1,12,83,1,5,3,2]

argument=[6,1,2,3,4,5]
print(buble_sort(argument))
                    