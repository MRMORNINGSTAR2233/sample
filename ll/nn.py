def display_heart_with_name(name):
    heart = '''
     ********         ********
   **        **     **        **
 **            ** **            **
**               *               **
**                               **
 **                             **
   **                         **
     **                     **
       **                 **
         **             **
           **         **
             **     **
               ** **
                 *
'''

    heart_with_name = heart.replace('*', name.center(8, ' '))
    print(heart_with_name)


if __name__ == "__main__":
    your_name = input("Enter your name: ")
    display_heart_with_name(your_name)
