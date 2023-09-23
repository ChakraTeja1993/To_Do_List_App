import register_signin

def main():
    while True:
       user_preference = input("Select your preference\n1.signin 2.register 3.exit\n")
       if user_preference == str(1):
            register_signin.signin()
       elif  user_preference == str(2):
            register_signin.register()
       elif user_preference == str(3):
           break
       else: print("\n****invalid choice! Try again****\n")

main()