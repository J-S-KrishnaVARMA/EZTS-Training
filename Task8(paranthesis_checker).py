text=input("Enter your expression:")
def valid(text):
    text=str(text)
    stack=[]
    j=-1
    for i in text:
        if i=="(" or i=="[" or i=="{":
                j+=1
                stack.append(i)

        elif i==")":
            if stack[j]=="(":
                stack.pop(j)
                j-=1
        elif i=="]":
            if stack[j]=="[":
                stack.pop(j)
                j-=1
        elif i=="}":
            if stack[j]=="{":
                stack.pop(j)
                j-=1
                
        print(stack)
    if len(stack)!=0:
        return "Invalid expression as open brackets do not match closing ones"
        
            
    
    return "Its a valid statement"
print(valid(text))
