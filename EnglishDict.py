import json
from difflib import get_close_matches

#Accesing the json dictionary and storing its data in a dictionary type variable data
data = json.load(open("E:\Python projects\English Dictionary\data.json"));

def translate(word):
    #To check whether word present or not.
    word=word.lower()
    if word in data: 
        return(data[word])
    elif len(get_close_matches(word,data.keys())) > 0 :  #If wrong word entered then we get the closest possible word
      yn = input("Did you mean %s ? Enter (Y/N)" % get_close_matches(word,data.keys())[0]) 
      if yn == "Y" :
          return data[get_close_matches(word,data.keys())[0]]
      elif yn == "N":
        return ("The word is not present in our Dictionary. Please recheck it.") 
      else:
          return "Please enter Y or N !!"   

ans = "Y"
while(ans=="Y"):
    word = input("Enter word: ")
    output = translate(word)
    #Print without [] and ''
    if type(output) == list: 
        print(get_close_matches(word,data.keys())[0].upper()+":- ")
        for i in output:
            print(i)
    else:
            print(output)    

    ans = input("Do you wish to continue?(Y/N)")