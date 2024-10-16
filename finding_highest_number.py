#FUNCTION find_highest_number(num1, num2, num3, num4, num5)
    #IF num2 > num1 THEN
        #SET highest TO num2
    #ELSE
        #SET highest TO num1

    #IF num3 > highest THEN
        #SET highest TO num3

    #IF num4 > highest THEN
        #SET highest TO num4

    #IF num5 > highest THEN
        #SET highest TO num5

    #RETURN highest
#END FUNCTION

def find_highest_number(num1, num2, num3, num4, num5):
    
    if num2 > num1:
        highest = num2
    else:
        highest = num1
