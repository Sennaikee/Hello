name = input("Enter your name: ")
print("Welcome {}".format(name.title()))
should_continue = True
continue_adding = True
while should_continue:
    print("\nWhat arithmetic operation would you like to do:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modulo Division\nTYPE 'EXIT' TO END PROGRAM")
    continue_adding = True
    op = input("> ")
    if op == "1":
        print("Type quit to stop addition")
        while continue_adding:
            nums = input("Enter the numbers you want to add (separated by a space): ").lower().split(" ")
            if 'quit' in nums:
                continue_adding = False
            else:
                plus = 0
                for num in nums:
                    plus = plus + int(num)
                print(plus)

    elif op == "2":
        print("Type quit to stop subtraction")
        while continue_adding:
            nums = input("Enter the numbers you want to subtract(separated by a space): ").lower().split(" ")
            if 'quit' in nums:
                continue_adding = False
            else:
                for num in nums:
                    sub = int(nums[0])
                    sub = sub - int(num)
                print(sub)

    elif op == "3":
        print("Type quit to stop multiplication")
        while continue_adding:
            nums = input("Enter the numbers you want to multiply(separated by a space): ").lower().split(" ")
            if 'quit' in nums:
                continue_adding = False
            else:
                multi = 1
                for num in nums:
                    multi *= int(num)
                print(multi)

    elif op == "4":
        while continue_adding:
            print("Type quit to stop division")
            nums = input("Enter the numbers you want to divide(separated by a space): ").lower().split(" ")
            if 'quit' in nums:
                continue_adding = False
            else:
                for num in nums:
                    div = int(nums[0])
                    div /= int(num)
                print(div)

    elif op == "5":
        while continue_adding:
            print("Type quit to stop modulo division")
            nums = input("Enter the numbers you want to do modulo operation on(separated by a space): ").lower().split(" ")
            if 'quit' in nums:
                continue_adding = False
            else:
                for num in nums:
                    mod = int(nums[0])
                    mod %= int(num)
                print(mod)

    elif op == "exit":
        should_continue = False
        print("Exiting the program...\nGoodbye {}".format(name.title()))

    else:
        print("Invalid operation type.")
