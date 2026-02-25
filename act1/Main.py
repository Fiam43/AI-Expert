print("Hello! I am AI Bot. What's your name? :")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) : ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. I hope things get better soon.")
else: 
    print("I see. Sometimes it's hard to put feelings into words.")

print("Do you like playing ? (yes/no):")
playing = input().lower()

if playing == "yes":
    print("That's great! Playing can be a lot of fun.")
elif playing == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("what is your favourite day ? (sun/mon/tue/wed/thu/fri/sat):")
day = input().lower()

if day == "sun":
    print("Sunday is a great day to relax!")
elif day == "mon":
    print("Monday can be tough, but it's the start of a new week.")
elif day == "tue":
    print("Tuesday is a good day to get things done.")
elif day == "wed":
    print("Wednesday is the middle of the week, keep going!")
elif day == "thu":
    print("Thursday is almost the weekend, almost there!")
elif day == "fri":
    print("Friday is a great day to finish up work and prepare for the weekend.")
elif day == "sat":
    print("Saturday is a perfect day to have fun and relax.")
else:
    print("I see. That's fine too.")

print("Do you like kids or adults ? (k/ad):")
preference = input().lower()

if preference == "k":
    print("That's great! Kids are fun to play with.")
elif preference == "ad":
    print("That's okay! Adults are also fun to play with.")
else:
    print("I see. That's fine too.")

print("Do you like dogs or cats ? (d/c):")
pet_preference = input().lower()

if pet_preference == "d":
    print("Dogs are loyal and friendly companions!")

elif pet_preference == "c":
    print("Cats are independent and graceful pets!")

else:
    print("I see. That's fine too.")

print("Do you like shopping ? (yes/no):")
s = input().lower()

if s == "yes":
    print("That's great! Shopping can be a lot of fun.")
elif s == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("Do you like travelling ? (yes/no):")
t = input().lower()

if t == "yes":
    print("That's great! Travelling can be a lot of fun.")
elif t == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("Do you like music ? (yes/no):")

m = input().lower()

if m == "yes":
    print("That's great! Music can be a lot of fun!")

elif m == "no":
    print("That's okay! Everyone has different interests.")

else:
    print("I see. That's fine too.")

print("Do you like movies ? (yes/no):")
movies = input().lower()

if movies == "yes":
    print("That's great! Movies can be a lot of fun.")
elif movies == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("Do you like baking ? (yes/no):")
baking = input().lower()

if baking == "yes":
    print("That's great! Baking can be a lot of fun.")
elif baking == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("Do you like coding ? (yes/no):")
coding = input().lower()

if coding == "yes":
    print("That's great! Coding can be a lot of fun.")
elif coding == "no":
    print("That's okay! Everyone has different interests.")
else:
    print("I see. That's fine too.")

print("Would you like to chat with me all day long ? (yes/no):")
chat = input().lower()

if chat == "yes":
    print("That's great! I'm happy to chat with you all day long.")
elif chat == "no":
    print("That's okay! I know you might be busy or tired.")
else:
    print("I see. That's fine too.")

print(f"It was nice chatting with you {name}. Goodbye!")

