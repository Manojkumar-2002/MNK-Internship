x = 10  

def update_x():
    try:
        print(x)  
        x = x + 1  
    except UnboundLocalError as e:
        print(e)
    

update_x()
