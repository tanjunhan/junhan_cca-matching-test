print("Title of program: CCA Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest a CCA for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

tech1 = input("I enjoy building and fixing things.")

outdoor1 = input("I'll go crazy if I do not go out of the house for the whole day.")

music1 = input("I can see colours in my mind when i hear music.")

uniform1 = input("I can follow orders and instructions given to me.")

tech2 = input("I know how to build apps and websites.")

outdoor2 = input("I'm good with tying knots and ropes.")

music2 = input("I play a musical instrument well.")

uniform2 = input("I know the drills well.")

tech3 = input("I enjoy coding and doing computing.")

outdoor3 = input("I love hiking.")

music3 = input("I like to listen to different/all kinds of music.")

uniform3 = input("I can execute drills well.")



tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1)+ int(music2) + int(music3)
uniform_final = int(uniform1)+ int(uniform2) + int(uniform3)

print()

if tech_final > outdoor_final and tech_final > music_final and tech_final > uniform_final:
  print("You might be suitable for Infocomm club!")
if outdoor_final > music_final and outdoor_final > tech_final and outdoor_final > uniform_final:
  print("You might be stuiable for Outdoor Adventure Club!")
if music_final > tech_final and music_final > outdoor_final and music_final > uniform_final:
  print("You might be suitable for Band!") 
if uniform_final > music_final and uniform_final > tech_final and uniform_final > outdoor_final:
    print("You might be suitable for NPCC!")
    
   

  
