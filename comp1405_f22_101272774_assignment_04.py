#Hirad Showghi
#101272774
#The code runs perfectly fine on https://www.programiz.com/python-programming/online-compiler/ and 
#IDE but not in terminal and I couldn't figure out why. I was using testing out the website becuase 
#it, I would appreciate if you could mark it on the website because that is where I was coding 
#was much easier to work with 
#Movie subgenres chosen: Super Heroes and Sci-Fi Action

print("Welcome to the movie guesser 3000! We are going to play a game where I will ask questions in order 
to guess the movie you choose.")
#The 2 subgenres: Superhero & Sci-Fi Action
print("First pick a subgenre: Superhero or Sci-Fi Action")
subgenre=input()

if subgenre in ['superhero', 'Superhero', 'SUPERHERO']:
    #The list of 10 movies chosen for the superhero subgenre
     print("Great! Now choose one of the movies from the Superhero subgenre: The Batman, Batman: The 
Dark Knight, Batman: The Dark Knight Rises, Spiderman 2, Spiderman 3, Spiderman: Homecoming, The 
Avengers, Avengers: Age of Ultron, Avengers: Infinity War, Avengers: Endgame.")
     #Marvel has created all the avengers and spiderman movies from the list above
     print("Awesome, now tell me, is your movie based on the marvel universe?") 
yes_or_no1=input()
if yes_or_no1 == 'yes' or yes_or_no1 =='YES' or yes_or_no1 =='Yes':
    #Thanos makes an appearance in all Avengers movies
    print("Okay...does the villain Thanos make an appearance in the movie?")
    yes_or_no2=input()
    if yes_or_no2 == 'yes' or yes_or_no2 =='YES' or yes_or_no2 =='Yes':
        #Iron man dies in Avengers Endgame.
        print("Does Iron Man die in your movie?") 
        yes_or_no3=input()
        if yes_or_no3 == 'yes' or yes_or_no3 =='YES' or yes_or_no3 =='Yes':
            print("Your movie is Avengers: Endgame.")
        elif yes_or_no3 == 'no' or yes_or_no3 =='NO' or yes_or_no3 =='No':
            print("Did your movie feature Spiderman as one of the Avengers?")
            yes_or_no4=input()
            if yes_or_no4 == 'yes' or yes_or_no4 =='YES' or yes_or_no4 =='Yes':
                #Spiderman is part of the Avengers in Infinity war.
                print("Your movie is Avengers: Infinity War.")
            elif yes_or_no4 == 'no' or yes_or_no4 =='NO' or yes_or_no4 =='No':
                print("Was your movie released in 2012?")
                yes_or_no5=input()
                if yes_or_no5 == 'yes' or yes_or_no5 =='YES' or yes_or_no5 =='Yes':
                    print("Your movie is Avengers.")
                elif yes_or_no5 == 'no' or yes_or_no5 =='NO' or yes_or_no5 =='No':
                    print("Your movie is Avengers: Age of Ultron.")
    elif yes_or_no2 == 'no' or yes_or_no2 =='NO' or yes_or_no2 =='No':
        print("Does Toby Maguire play as spiderman in your movie?")
        yes_or_no6=input()
        if yes_or_no6 == 'yes' or yes_or_no6 =='YES' or yes_or_no6=='Yes':
            print("Does your movie feature a Villain Doctor?")
            yes_or_no7=input()
            if yes_or_no7 == 'yes' or yes_or_no7 =='YES' or yes_or_no7=='Yes':
                print("Your movie is Spiderman 2.")
            elif yes_or_no7 == 'no' or yes_or_no7 =='NO' or yes_or_no7=='No':   
                print("Your movie is Spiderman 3")
        elif yes_or_no6 == 'no' or yes_or_no6 =='NO' or yes_or_no6=='No':
            print("Your movie is Spiderman: Homecoming.")
           
elif yes_or_no1 == 'no' or yes_or_no1 =='NO' or yes_or_no1 =='No':  
    print("Is joker the villain in your movie?")
    yesno=input()
    if yesno == 'yes' or yesno =='YES' or yesno =='Yes':
        print("Your movie is Batman: The Dark Knight.")
    elif yesno == 'no' or yesno =='NO' or yesno =='No': 
        print("Does Christian Bale play Batman in your movie?")
        yesno1=input()
        if yesno1 == 'yes' or yesno1 =='YES' or yesno1 =='Yes':
            print("Your movie is Batman: The Dark Knight Rises.")
        elif yesno1 == 'no' or yesno1 =='NO' or yesno1 =='No':
            print("Your movie is The Batman")
            
if subgenre in ['Sci-Fi Action', 'sci-fi action', 'SCI-FI ACTION']:
    #The list of 10 movies chosen for the superhero subgenre
     print("Great! Now choose one of the movies from the Sci-Fi Action subgenre: The Hunger Games, 
The Hunger Games: Catching Fire, The Hunger Games: Mocking Jay Part 1, The Hunger Games: Mocking Jay 
Part 2, Interstellar, The Martian, Passengers, Jurassic Park , Jurassic Park III, Jurassic World 
Dominion")
     print("Awesome, now tell me, is your movie set in outter space?") 
answer=input()
if answer == 'yes' or answer =='YES' or answer =='Yes':
    print("Okay...Do the 2 main characters fall in love?")
    answer2=input()
    if answer2 == 'yes' or answer2 =='YES' or answer2 =='Yes':
        #Iron man dies in Avengers Endgame.
        print("Your movie is Passengers.")
    elif answer2 == 'no' or answer2 =='NO' or answer2 =='No':
            print("Is Matt Damon an actor in your movie?")
            answer3=input()
            if answer3 == 'yes' or answer =='YES' or answer =='Yes':
                print("Your movie is The Martian.")
            elif answer3 == 'no' or answer3 =='NO' or answer3 =='No':
                print("Your movie is Interstellar.")
elif answer == 'no' or answer =='NO' or answer =='No':    
    print("Does the main character wield a bow?")
answer3=input()
if answer3 == 'yes' or answer3 =='YES' or answer3 =='Yes':
    print("Does she get volunteer as tribute for District 12")
    answer4=input()
    if answer4 == 'yes' or answer4 =='YES' or answer4 =='Yes':
        print("Your movie is The Hunger Games.")
    elif answer4 == 'no' or answer4 =='NO' or answer4 =='No':
        print("Does the main character pose as a symbol of peace between districts?")
        answer5=input()
        if answer5 == 'yes' or answer5 =='YES' or answer5 =='Yes':
            print("Did your movie come out in 2014")
            answer6=input()
            if answer6 == 'yes' or answer5 =='YES' or answer5 =='Yes':
                print("Your movie is The Hunger Games: Mocking Jay Part 1.")
            elif answer6 == 'no' or answer6 =='NO' or answer6 =='No': 
                print("Your movie is The Hunger Games: Mocking Jay Part 2.")
        elif answer5 == 'no' or answer5 =='NO' or answer5 =='No': 
            print("Your movie is The Hunger Games: Catching Fire.")
elif answer3 == 'no' or answer3 =='NO' or answer3 =='No':
    print("Did your movie release in 2001?")
    answer7=input() 
    if answer7 == 'yes' or answer7 =='YES' or answer7 =='Yes':
        print("Your movie is Jurassic Park III.")
    elif answer7 == 'no' or answer7 =='NO' or answer7 =='No': 
        print("Is Chris Pratt an actor in your movie?")
        answer8=input()
        if answer8 == 'yes' or answer8 =='YES' or answer8 =='Yes':
            print("Your movie is Jurassic World Dominion?")
        elif answer8 == 'no' or answer8 =='NO' or answer8 =='No':
            print("Your movie is Jurassic Park.")  
