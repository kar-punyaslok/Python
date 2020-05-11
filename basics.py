msg="Say something: "
messages=[]
while True:
    if(input(msg)=="stop"):
        break
    else:   
            messages.append(input(msg))
        
print(messages)