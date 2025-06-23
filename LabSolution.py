def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print(f"The variable used in the add is not valid: {e} ")
    else:
        print("The operation is successful")
        
additoin(10, 20)
