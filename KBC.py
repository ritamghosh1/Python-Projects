# Displaying the Rules
print("Welcome to \" Kaun Banega CrorePati \"" )
input() 
print("Here are the rules of the game ")
input() 
print("1. There will be three rounds of the game")
input() 
print("2. At first you have to choose the Catagory at the start of each round")
input() 
print("3. You will be displayed three questions of the catagory of which you have to give the right answer of ")
input() 
print("4. If you give the right answer you will get $100 else you'ii get no money")
input() 
print("5. You'll have three lives, if you lost all your lives the game will stop there" )
input() 
name = input("Enter Your Name :")
def KBC(name : str):
    # Setting Up the Game
    print("Welcome Mr. / Mrs./ Miss",name)
    lives = 3 
    count = 0 
    catagory = ["Science", "Physics", "History"]
    print("You can choose from the following catagories",catagory,count)
    selected_catagory = str(input("Please Enter the catagory"))
    sc = ["Which among the following acids is abundant in Grapes, Bananas and Tamarind?   [A] Lactic Acid    [B] Oxalic Acid   [C] Salicylic Aci [D] Tartaric Acid" , " Who was the first woman to win a Nobel Prize in Literature?   [A] Marie Antoinette    [B] Sir William Shakespeare    [C] Marie Curie   [D] Louis XVI"
          , "Work done is defined as the dot product of which of the following vectors?   [A] Force and acceleration    [B] Force and area     [C] Force and instantaneous velocity    [D] Force and displacement"]
    sc_ans = ["D", "C" , "D"]
    his = ["During whose reign Gandhāran style of art flourished?   [A] Guptas   [B] Hunas   [C] Satavahana   [D] Kushans",
           "At which among the following places, Chandragupta Maurya spent his last days?  [A] Nalanda   [B] Ujjain   [C] Shravana Belgola   [D] Kashi",
           "What is the birthplace of Napolean? [A] Sicilly [B] Paris [C] Vienna [D] Germany"]
    his_ans = ["D","C","A",]
    phy = ["When light from some sources enters to the earth’s atmosphere, it gets scattered. Which among the following is a reason behind scattering?  [A] Various wavelengths of light    [B] dust, smoke and gas molecules    [C] atmospheric pressure    [D] None of the above"
            "Speed of light will be maximum in which of the following mediums?  [A] Water  [B] Kerosene  [C] Flint Glass  [D] Diamond"
             "4.Who discovered the moons of Jupiter ?   [A] Isaac Newton  [B] Archimedes  [C] Albert Einstein  [D] Galileo Galilei" ]
    phy_ans = ["B","A","D"]
    for i in range(3):
        match i :
            case 0 : print("This is the first Round , All the best")
            case 1 : print("This is the second Round , Be Careful")
            case 2 : print("This is the third Round , We are close to Victory")
        # If the Player had selected the Science Catagory
        l = 0
        j = 0
        k = 0
        if(selected_catagory == "Science"):
            while(j<3):
                print(sc[j])
                ans = input("Your Answer : ")
                if(ans == sc_ans[sc.index(sc[j])]):
                    count += 1
                    print("Congratulations!!! You Gain $100")
                else:
                    count -= 1 
                    lives -= 1
                    print("Sorry!!! You Lose $100")
                if lives == 0:
                    print("Game Over!!! You Lost All Your Lives")
                    break
                j += 1
        # If the Player had selected the History Catagory
        if(selected_catagory == "History"):
            while(l<3):
                print(his[l])
                ans = input("Your Answer : ")
                if(ans == his_ans[his.index(his[i])]):
                    count += 1
                    print("Congratulations!!! You Gain $100")
                else:
                    count -= 1 
                    lives -= 1
                    print("Sorry!!! You Lose $100")
                if lives == 0:
                    print("Game Over!!! You Lost All Your Lives")
                    break
                l += 1
        # If the Player had selected the Physics Catagory
        if(selected_catagory == "Physics") :
           while(k<3):
               print(phy[k])
               ans = input("Your Answer : ")
               if(ans == phy_ans[phy.index(phy[k])]):
                   count += 1
                   print("Congratulations!!! You Gain $100")
               else :
                   count -= 1 
                   lives -= 1
                   print("Sorry!!! You Lose $100")
               if lives == 0:
                    print("Game Over!!! You Lost All Your Lives")
                    break
               k += 1
        catagory.remove(selected_catagory)
        print(catagory)
        selected_catagory = str(input("Please Enter the catagory"))
    if(count>0) : print("Congratulations!!! You have earned $"+(count*100))
    else: print("Sorry!!! You haven't won any money")

KBC(name)