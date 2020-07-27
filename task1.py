while True:
    input_str = input('Input sting ')
    if input_str == "":
        print("Bye!")
        exit()
    try:
        with open("task1.txt", 'a') as f_obj:
            if not f_obj.writable():
                print ("File is not writable")
                exit()
            print(input_str, file=f_obj)
    except:
        print("Some error with file!")

