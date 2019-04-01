from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
chatbot = ChatBot('Fred')
chatbot2 = ChatBot('lisa')
# Holds all chatbotfactory objects
holder = []
chatbotdev = []
class ChatbotFactory:
    #Constructor for ChatbotFactory objects
    def __init__(self,number):
        self.number = number
    #Trains a given object
    def learn(self, chatterbot):
        #implements data found in corpus for each object
        trainer = ListTrainer(chatterbot)
        #Stores data from corpus
        conversation = open('English_Chats.yml','r').readlines()
        conversation2 = open('German_Chats.yml', 'r').readlines()
        #Uses corupus to upload possible responses to chatbot
        trainer.train(conversation)
        trainer.train(conversation2)
    # Takes last response and uses that to generate new response
    def listen(self,test,test2,num):
        #Last response made by a chatbot
        print(num," current response is:", test)
        #generates a new response based on previous response made by other chatbot
        response = test2.get_response(test)
        print(response)
        return response
    #Appends new ChatbotFactory object to holder list
class Chatbotcreator():
    def create(self,x,y,z):
        #Adds new chatbot to the list to be called
        x.append(ChatbotFactory(y))
        #Makes new storage for corpus information
        dev = ChatBot(str(y))
        #Stores variable previously made into a list.
        # The chatbot variable will be called alongside a class object in the holder list that shares the same index code
        z.append(dev)
def main():
    print("Welcome to our Chatterbot civilization. In this program, we will demonstrate to you the interaction and reproduction of chatterbots.")
    print("The chatbots use the same mind, so it looks as if they are speaking as one, and not as an individual. This is due to us using the same 'mind' to make replication easier.")
    print("In the real world, this chatbot could be used to help mimmick real life conversations with people, so that people could use it to train and learn different languages")
    #Creates new objects(bots) of class Chatbotfactory
    god = Chatbotcreator()
    #Fred and Lisa are the first to be placed into the list. The list will always start with these two speaking. Fred is 0 and Lisa is 10. This is just to help initialize them
    fred = ChatbotFactory(0)
    lisa = ChatbotFactory(10)
    #Placing Fred in appendix 0 and lisa in appendix 1. The list should have 2 entries right now.
    holder.append(fred)
    holder.append(lisa)
    chatbotdev.append(chatbot)
    chatbotdev.append(chatbot2)
    #Each object will be initialized by calling a specific part of the list. All objects will be stored in the list
    holder[0].learn(chatbot)
    holder[1].learn(chatbot2)
    #Starting phrase helps condition the chatbot to not repeat phrase. Changing phrase to something not in either corpus's will cause chatbot to repeat a phrase forever
    read = holder[0].listen("Are you an AI?",chatbot,0)
    while True:
        #Is used to track where we are on the list. Helps determine when we have reached the end of the list
        y = 0
        while y != len(holder):
            #Slows down output flow
            time.sleep(1)
            read = holder[y].listen(read,chatbotdev[y],y)
            #Every time we use an object in the list, we iterate to the next object. Once we reached the last object, we fall out of the loop
            y = y + 1
        # When we drop out of the loop we append to the list another chatbot instance
        god.create(holder,y,chatbotdev)
        z = 0
        while z != len(holder):
            #The new chatbots are untrained, so, in order for them to work properly, we need to train them.
            holder[z].learn(chatbotdev[z])
            z = z + 1

main()