
# Add Two Numbers 

# l1=[2,4,3]
# l2=[5,6,4] 

def add(l1,l2) :
    
    return l1+ l2

ans=add(243,564)

convert_str=str(ans)
rev=''.join(reversed(convert_str))

# convert_int=int(rev)


convert_list=list(rev)
convert_list=(rev for i in convert_list) 
print(convert_list )





