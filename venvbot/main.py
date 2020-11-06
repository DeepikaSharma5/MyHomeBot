from functions import *

#  chatbot Emily
home_bot = create_bot('Emily')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please(Name) : ")

# identity rules
if identity == "Deepika":
    print("Welcome, Deepika. Happy to have you at home. Please sanitize your hands and clean your body.")

elif identity == "Sanam":
    print("Mark is out right now, but you are welcome to the house.")

else:
    print("Your access is denied here.")
    exit()

# public data. Deepika and sanam can access
house_owner = [
    "Who is the owner of this house?",
    "Deepika Srinivasan is the owner of this house."
]

night = [
    "Good night",
    "Good night. Have a wonderful dream"
]

bye = [
    "Bye.Catch you later",
    "Bye. Enjoy ypur day."
]
custom_train(home_bot, house_owner)
custom_train(home_bot, night)
custom_train(home_bot, bye)

print("------ Training custom data ------")

# Only deepika can access these
if identity == 'Deepika':   
    city_born = [
        "Where was I born?",
        "Deepika, you were born in Gampaha."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is Winter Walters by Allen & Unwin."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Aashiqui-2 more than 100 times."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved basketball."
    ]

    bill = [
        "Do I need to pay any bills this month?",
        "You need to pay WI-FI bill."
    ]

    price = [
        "Is the bill price high?",
        "Yes, You need to stop wasting WI-FI by watching YouTube."
    ]

    parent = [
        "Who do you think your parents are?",
        "You Invented me. So you are my parent. - With LOVE - "
    ]

    name = [
        "Do you like your name?",
        "Emily is a nice name. I think you gave me this name after watching 'Emily in Paris'."
    ]

    fav_place = [
        "Do you know my favourite place?",
        "I think everyone who is closer to you knows that. PARIS - the city of love."
    ]

    bored = [
        "I am bored.",
        "I can sing you a song if you implement voice for me."
    ]

    nexts = [
        "I'll do that as my next sample project.",
        "Thankyou for your concern on me."
    ]

    work = [
        "I have a lot to do today.",
        "I know you can do it. Take small breaks between work."
    ]

    fine = [
        "How are you Emily?",
        "Fine, Little bored without you."
    ]

    sports = [
        "What do you thing the best sports is?",
        "Maybe Cricket. Because most of the people like that and it is somehow interesting."
    ]

    sleep = [
        "Ok I have work to do",
        "Catch me if you get free."
    ]

 
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, bill)
    custom_train(home_bot, price)
    custom_train(home_bot, parent)
    custom_train(home_bot, name)
    custom_train(home_bot, fav_place)
    custom_train(home_bot, bored)
    custom_train(home_bot, work)
    custom_train(home_bot, fine)
    custom_train(home_bot, sports)
    custom_train(home_bot, sleep)
    custom_train(home_bot, nexts)
    custom_train(home_bot, fine)
    


# start chatbot Emily
start_chatbot(home_bot)