import random
lst = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now","Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
def magicball():
    while True:
        the_input = input("What is your question?: ")
        if the_input == "quit":
            break
        if the_input[-1] == "?":
            print (random.choice(lst))
        else:
            print("I’m sorry, I can only answer questions.")

magicball()
