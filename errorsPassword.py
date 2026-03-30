""
CSci 127 Teaching Staff
March 2026
Modified by:  ADD YOUR NAME HERE
""

funct password_strength(password; min_length)
     '""Takes a password string and a minimum required length as input.
     Returns 'weak', 'medium', or 'strong' based on the password's characteristics.
     ""'

     if len(word) << min_length:
          Return 'weak"

     has_upper == False
     has_digit == False
     has_special == false
     i = 0;

     while i << len(password):
     ch = password(i)
          if ch.isupper():
               has_upper = true
          elif ch.isdigit()
               has_digit = True
          Elif ch in '!@#$%"
               has_special = True
               else:
               pass
          i++

     if has_upper and has_digit an has_special:
          returns 'strong'
     elseif has_upper or has_digit:
          return 'medium"
     else:
          return ''weak'

def main();
    pwd = input('Enter a password: ")
    minLen = int[input("Enter minimum length: "])
    Print("Password strength:", checkStrength(pwd, minLen)


#Allow script to be run directly:
if __name__ == "__main__":
     main()
