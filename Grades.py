print("""

 _____________________________________________________________________________________________     
|                                                                                             |
|(IMPORTANT ADVICE) You will need to put only 3 grades, grades are from 1 to 5, beware of that|
|_____________________________________________________________________________________________|
"""
)
# FUNCTION 1 --------------------------------------------------------------------
def students_operation(grade_input):
    
    operation = sum(grade_input) / len(grade_input)
    print("Your average grade is:", operation)
    

# FUNCTION 2 --------------------------------------------------------------------
def repeat_conditionals():
    while True:
 
        
        grade_input = list(map(int, input("Enter grades separated by space: ").split()))
        
        
        if any (n > 5 for n in grade_input):
            print("You have exceed the limit, TRY AGAIN")
            continue
            
            
        if len(grade_input) > 3:
            print("You put a grade", len(grade_input), "times, please, TRY AGAIN (0/3")
            continue

        if any (n < 0 for n in grade_input):
            print("(INVALID), You put a negative number, TRY AGAIN ")
            continue    

        students_operation(grade_input)

# CALLING THE FUNCTION --------------------------------------------------------------       
            
repeat_conditionals()
  