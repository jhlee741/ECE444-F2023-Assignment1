import main

test1 = main.utils(1)
test1.reversed()
test1.formatter()

test2 = main.utils(123456)
test2.reversed()
test2.formatter()

test3 = main.utils(123456.789)
test3.reversed()
test3.formatter()

test4 = main.utils("123456")
test4.reversed()
test4.formatter()

test5 = main.utils("testing word")
test5.reversed()
test5.formatter()

test6 = main.utils("1234abs56")
test6.reversed()
test6.formatter()

test7 = main.utils(0)
test7.reversed()
test7.formatter()

test8 = main.utils(5.3)
test8.reversed()
test8.formatter()

test9 = main.utils(25564)
test9.reversed()
test9.formatter()

test10 = main.utils(3567)
test10.reversed()
test10.formatter()

test1solution_r = "1"
test2solution_r = "654321"
test3solution_r = "This method only takes integers as an input"
test4solution_r = "This method only takes integers as an input"
test5solution_r = "This method only takes integers as an input"
test6solution_r = "This method only takes integers as an input"
test7solution_r = "0"
test8solution_r = "This method only takes integers as an input"
test9solution_r = "46552"
test10solution_r = "7653"

test1solution_f = "binary: 1 | octal: 1"
test2solution_f = "binary: 11110001001000000 | octal: 361100"
test3solution_f = "This method only takes integers as an input"
test4solution_f = "This method only takes integers as an input"
test5solution_f = "This method only takes integers as an input"
test6solution_f = "This method only takes integers as an input"
test7solution_f = "binary: 0 | octal: 0"
test8solution_f = "This method only takes integers as an input"
test9solution_f = "binary: 110001111011100 | octal: 61734"
test10solution_f = "binary: 110111101111 | octal: 6757"

pass_r = 0
pass_f = 0
fail_r = 0
fail_f = 0

#Reverser Tests
print("Running reverser tests...")
if str(test1.reversed_int) == test1solution_r:
    pass_r = pass_r +1
    print("Reverse Test 1: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 1: Fail")
if str(test2.reversed_int) == test2solution_r:
    pass_r = pass_r +1
    print("Reverse Test 2: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 2: Fail")
if str(test3.reversed_int) == test3solution_r:
    pass_r = pass_r +1
    print("Reverse Test 3: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 3: Fail")
if str(test4.reversed_int) == test4solution_r:
    pass_r = pass_r +1
    print("Reverse Test 4: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 4: Fail")
if str(test5.reversed_int) == test5solution_r:
    pass_r = pass_r +1
    print("Reverse Test 5: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 5: Fail")
if str(test6.reversed_int) == test6solution_r:
    pass_r = pass_r +1
    print("Reverse Test 6: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 6: Fail")
if str(test7.reversed_int) == test7solution_r:
    pass_r = pass_r +1
    print("Reverse Test 7: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 7: Fail")
if str(test8.reversed_int) == test8solution_r:
    pass_r = pass_r +1
    print("Reverse Test 8: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 8: Fail")
if str(test9.reversed_int) == test9solution_r:
    pass_r = pass_r +1
    print("Reverse Test 9: Pass")
else:
    fail_r = fail_r + 1
    print("Reverse Test 9: Fail")
if str(test10.reversed_int) == test10solution_r:
    pass_r = pass_r +1
    print("Reverse Test 10: Pass\n")
else:
    fail_r = fail_r + 1
    print("Reverse Test 10: Fail\n")


# Formatter Tests
print("Running formatter tests...")
if test1.formatter_string == test1solution_f:
    pass_f = pass_f +1
    print("Format Test 1: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 1: Fail")
if test2.formatter_string == test2solution_f:
    pass_f = pass_f +1
    print("Format Test 2: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 2: Fail")
if test3.formatter_string == test3solution_f:
    pass_f = pass_f +1
    print("Format Test 3: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 3: Fail")
if test4.formatter_string == test4solution_f:
    pass_f = pass_f +1
    print("Format Test 4: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 4: Fail")
if test5.formatter_string == test5solution_f:
    pass_f = pass_f +1
    print("Format Test 5: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 5: Fail")
if test6.formatter_string == test6solution_f:
    pass_f = pass_f +1
    print("Format Test 6: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 6: Fail")
if test7.formatter_string == test7solution_f:
    pass_f = pass_f +1
    print("Format Test 7: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 7: Fail")
if test8.formatter_string == test8solution_f:
    pass_f = pass_f +1
    print("Format Test 8: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 8: Fail")
if test9.formatter_string == test9solution_f:
    pass_f = pass_f +1
    print("Format Test 9: Pass")
else:
    fail_f = fail_f + 1
    print("Format Test 9: Fail")
if test10.formatter_string == test10solution_f:
    pass_f = pass_f +1
    print("Format Test 10: Pass\n")
else:
    fail_f = fail_f + 1
    print("Format Test 10: Fail\n")

if pass_r == 10 and pass_f == 10:
    print("All tests passed, congrats!")
elif pass_r == 10 and pass_f < 10:
    print("The reverser passed but not the formatter")
elif pass_r < 10 and pass_f == 10:
    print("The formatter passed but not the reverser")
elif pass_r < 10 and pass_f < 10:
    print("Both tests failed")

