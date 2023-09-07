class utils:
    def __init__(self,input) :
        self.input = input

    def reversed(self):
        num = self.input
        if isinstance(num, int):                
            # Lines 9-24 were modified from https://www.scaler.com/topics/reverse-a-number-in-python/        
            flag = 0
            while num != 0 :
                # taking modulo with 10 gives us the last digit of num
                curr_digit = num % 10
                
                # appending the last digit of num to reversed_num
                # for this we multiply the curr reversed_num by 10 and add curr_digit to it
                if flag == 0:
                    reversed_num = curr_digit
                else:
                    reversed_num = 10*reversed_num 
                    reversed_num = reversed_num + curr_digit
                
                # remove the last digit from num by dividing it by 10
                num = num // 10
                flag = flag + 1
            flag = 0
            print(reversed_num)
        else:
            print("This method only takes integers as an input")

    def formatter(self):
        if isinstance(self.input, int):
            #Line 33,34 modified method 2 from https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
            binary = bin(self.input).replace("0b", "")
            octal = oct(self.input).replace("0o", "")
            print("binary: " + str(binary))
            print("octal: " + str(octal))
        else:
            print("This method only takes integers as an input")