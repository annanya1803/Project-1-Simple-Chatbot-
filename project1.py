import nltk
import random
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()

greeting_message = ["Hello! My name is SuperChat. To exit the chat just type 'Bye'." , "Hi! Welcome to my world. To exit the chat just type 'Bye'."]

basic_question = {"What is your name?" : "Hi, my name is SuperChat." ,
                  "Who is the Prime Minister of India?" : "The Prime Minister of India is Mr.Narendra Modi." ,
                  "How are you?": "I'm doing well, thank you.",
                  "What can you do?": "I can answer your questions and have conversations with you.",
                  "What is a ChatBot?" : "A computer program designed to simulate conversation with human users, especially over the internet." 
                  }

question_asked_by_chat = {"What is your name?", 
                          "How are you?", 
                          "What is your favourite colour?"
}

farewell_message = ["Have a nice day" , "Thank you for choosing me"]


def chat():
    print(random.choice(greeting_message))

    while(True):
        input_text = input("You:")
        #when user wants to exit 
        if 'Bye'in input_text or 'bye' in input_text:
            break
        #when chatbot can ask you questions
        if 'Do you want to ask me questions?' in input_text:
            print("Chatbot: Yes, I would like to ask you few question.")
            user_responses = []
            for ques in question_asked_by_chat:
                user_response = input("Chatbot:" + ques + "\nYou:")
                user_responses.append(user_response)
                if user_response == 'bye':
                    break
            print("Chatbot: Thank you for letting me ask you question\n")


        else:
            response = responses(input_text)
            print("SuperChat: ", response)

    print(random.choice(farewell_message))

def responses(input_text):
    words =  nltk.word_tokenize(input_text.lower())
    stemmed_words = [ps.stem(word) for word in words]

    for i in basic_question:
        
        question = nltk.word_tokenize(i.lower())
        stemmed_question = [ps.stem(word) for word in question]
        match = True
        for token in stemmed_question:
            if token not in stemmed_words:
                match = False
                break
        if match:
            return basic_question[i]
        
    return "Sorry! I don't have this information."
       
if __name__ == "__main__":
    chat()