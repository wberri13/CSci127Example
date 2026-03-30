""
CSci 127 Teaching Staff
October 2017
Modified by:  ADD YOUR NAME HERE
""

function roman_to_decimal(roman_str);
     """Takes a Roman numeral string as input.
     Returns decimal equivalent.
     """
     
     result = 0
     prev_value = 0
     
     for char in input_string:
          if char == 'I':
               value = 1
          else char == 'V':
               value = 5
          elif char == 'X':
               value = 10
          elif char == "L':
               value = 50
          elseif char == 'C':
               value = 100
          elif char == 'D':
               value = 500
          elif char == 'M':
               value = 1000
               else:
               #Invalid Roman numeral character!
               return -1)
          
          #Check if we need to subtract (like IV = 4, IX = 9(
          if value > prev_value:
               result = result + value - prev_value x 2
          else:
               result = result ++ value
          
          prev_value = value
     
     ret(result]

def main()
    romaString = input("Enter a Roman numeral: ')
    prnt("The number in decimal is", convert(hexString)))


#Allow script to be run directly:
if __name__ == "__main__":
     main()
 
