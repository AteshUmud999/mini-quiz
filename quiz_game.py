import random
import re

class QuizGame:
    
    def is_valid(self,password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[@!$]).{6,}$"
        
        if bool(re.fullmatch(pattern,password)):
            return True
        else:
            return False
        

    def sign_up(self):
        while True:
            name = input('Create a username:  ').strip().lower()
            if not name:
                print('Username cannot be empty.')
                continue
            
            if ',' in name:
                print('Username cannot contain comma.')
                continue
            
            if len(name) > 20:
                print('Username must be less than 20 characters')          
                continue
            
            is_not_exist = True
            with open('users.txt','r',encoding='utf-8') as users:
                for i in users:
                    a=i.strip().split(',')
                    if name == a[0]:
                        print('This username is already taken. Please try another one.')
                        is_not_exist = False
                        break
            if is_not_exist:
                break
                
        
        

        
        
        while True:
            password = input('Create a strong password (must include A-Z, a-z, @!$ and 6+ characters): ').strip()
            
            if self.is_valid(password):
                break
            
            else:
                print('Invalid Password! Try Again')
            
        with open('users.txt', 'a', encoding='utf-8') as users:
                users.write(name + ',' + password + '\n')
                print("\nAccount created successfully!") 
            
        
        
    def sign_in(self):
        try:
            name=input('Enter username: ').strip().lower()
            password = input('Enter password: ').strip()
            with open('users.txt','r',encoding='utf-8') as users:
                our_list = users.readlines()
                is_Found = False
                for i in our_list:
                    a = i.split(',')
                    a[1] = a[1].strip()
                    if name == a[0] and password == a[1]:
                        is_Found = True
                        break
                if is_Found:
                    message = '\nLogin successful!'
                    print(message)
                    return True
                else:
                    message = 'Invalid username or password. Please try again.'
                    print(message)
                    
                    return False
        except:
            print("Something went wrong during login.")
            return False
            
                    
                
                    

                
            
                
    def quiz(self):
        try:
            score = 0
            wrong_list =[]
            with open('questions.txt','r',encoding='utf-8') as q:
                questions_list = q.readlines()

            with open('mcq.txt','r',encoding='utf-8') as m:
                mcq_list = m.readlines()

            with open('answers.txt','r',encoding='utf-8') as a:
                answers_list = a.readlines()
                
            indexes = random.sample(range(len(questions_list)),5)
                
            for i in indexes:
                print("\n" + "-" * 50)
                print(questions_list[i].strip())
                print()
                print(mcq_list[i].strip())

                while True:
                    
                
                    user_answer = input('\nSelect your answer (A, B, C, or D): ').upper().strip()
                    
                    if user_answer in ['A','B','C','D']:
                        break
                    
                    print('Invalid choice! Please enter only A, B, C or D.')

                if user_answer == answers_list[i].strip():
                    print('\nCorrect answer! 🎉')
                    score += 1
                else:
                    wrong = [questions_list[i].strip(), user_answer, answers_list[i].strip()]
                    wrong_list.append(wrong)  
            print("\n" + "=" * 50)   
            print(f'Your final score: {score}/5')
            print('=' * 50)      
            if len(wrong_list) != 0:
                print('\nReview of Incorrect Answers:')
                for i in range(len(wrong_list)):
                    print(f'Question: {wrong_list[i][0].strip()}')
                    print(f'Your Answer: {wrong_list[i][1]}')
                    print(f'Correct Answer: {wrong_list[i][2].strip()}')
                    print('-' * 50)
                    
        except:
            print('Quiz error occurred.')  
  

game=QuizGame()

while True:
    print('=' * 50)
    print('     Welcome to Quiz Game')
    print('=' * 50)
    print('1.Sign Up\n2.Sign In\n3.Exit')


    answer = input('\nChoose one(1,2 or 3)').strip()



    try:

        if answer == '1':
            print("\n--- SIGN UP ---")
            game.sign_up()
        elif answer == '2':
            print("\n--- SIGN IN ---")
            result = game.sign_in()
            if result == True:
                print("\n" + "=" * 50)
                print("           QUIZ IS STARTING!")
                game.quiz()
                
                
                
                
                    
        elif answer == '3':
            print("\nThank you for playing Quiz Game!")
            break 
        
        else:
            print('\nInvalid choice! Please enter only 1, 2 or 3.')                   
                    
    except:
        print("\nUnexpected error occurred. Please try again.")

    
    




    

