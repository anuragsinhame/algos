def generate_fibonacci(no_of_terms):
    fibonacci_list = []
    first_term = 0
    second_term = 1
    if(no_of_terms>2):
        fibonacci_list.append(first_term)
        fibonacci_list.append(second_term)
        for i in range(2,no_of_terms):
            temp = first_term
            first_term = second_term
            second_term = temp+first_term
            fibonacci_list.append(second_term)
    elif(no_of_terms==2):
        fibonacci_list.append(first_term)
        fibonacci_list.append(second_term)
    elif(no_of_terms==1):
        fibonacci_list.append(first_term)
    
    for num in fibonacci_list:
        print(num)

generate_fibonacci(15)
