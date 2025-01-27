def abc():
    a = "Hello"
    try:
        print(a[10])
    except IndexError:
        print("Index out of range")
        
abc()
    