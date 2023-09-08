class utils:
    reversed_int = None
    formatter_string = None

    def __init__(self,input) :
        self.input = input

    def reversed(self):
        num = self.input
        if isinstance(num, int):                
            # Lines 16-29 were modified from https://www.scaler.com/topics/reverse-a-number-in-python/        
            flag = 0
            if num == 0:
                self.reversed_int = 0
            else:
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
                self.reversed_int = reversed_num
                #print(reversed_num)
        else:
            self.reversed_int = "This method only takes integers as an input"
            #print("This method only takes integers as an input")

    def formatter(self):
        if isinstance(self.input, int):
            #Line 41,42 modified method 2 from https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
            binary = bin(self.input).replace("0b", "")
            octal = oct(self.input).replace("0o", "")
            formatter_out = "binary: " + str(binary) + " | " + "octal: " + str(octal)
            self.formatter_string = formatter_out
            #print(formatter_out)
        else:
            self.formatter_string = "This method only takes integers as an input"
            #print("This method only takes integers as an input")

#test = utils(0)
#test.reversed()
#print(test.reversed_int)
