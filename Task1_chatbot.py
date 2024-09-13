import random

def chatbot():
    # Asking for the user's name to personalize the conversation
    user_name = input("Chatbot: Hello! What's your name?\nYou: ")
    
    print(f"Chatbot: Nice to meet you, {user_name}! How can I help you today?")
    
    # Dictionary for questions and answers with personal touches
    qa_pairs = {
        "hello": f"Hi there, {user_name}! How can I assist you today?",
        "hi": f"Hello, {user_name}! What's on your mind?",
        "how are you": f"I'm doing great, {user_name}! How about you?",
        "what's your name": f"I'm a simple rule-based chatbot, and I know I'm chatting with {user_name}!",
        "who are you": f"I'm a chatbot here to assist you, {user_name}.",
        "where are you from": "I know you're chatting with me from somewhere interesting!",
        "bye": f"Goodbye, {user_name}! Have a wonderful day!",
        "exit": f"Take care, {user_name}! Hope to see you soon!",
        "what can you do": f"I can answer basic questions and chat with you, {user_name}.",
        "how old are you": "I'm ageless, but I can tell you're full of life, {user_name}!",
        "who created you": "I was created by Muskan Narayan, a developer from Patna, Bihar. She's 24 years old and loves singing and painting!",
        "do you like singing": f"I know my creator Muskan loves singing, and I bet you'd enjoy it too, {user_name}.",
        "tell me a joke": random.choice([
            f"Why don't artists ever go hungry, {user_name}? Because they always find something to draw!",
            f"Why was the math book sad, {user_name}? Because it had too many problems.",
            f"What do you call a singer who doesn't like cheese, {user_name}? A rapper without a cheddar."
        ]),
        "what is ai": "AI stands for Artificial Intelligence, which is what makes me work!",
        "what is python": "Python is a popular programming language, great for building things like me.",
        "who is elon musk": "Elon Musk is the CEO of SpaceX and Tesla, famous for innovation.",
        "what is the capital of india": "The capital of India is New Delhi.",
        "who is the prime minister of india": "Narendra Modi is the Prime Minister of India.",
        "tell me about yourself": f"I'm a chatbot made by Muskan Narayan to assist people like you, {user_name}.",
        "what is love": "Love is a beautiful thing, but everyone experiences it differently.",
        "can you help me with math": "Sure! Ask me a basic math problem.",
        "what is 2 plus 2": "2 plus 2 equals 4.",
        "what is the square root of 16": "The square root of 16 is 4.",
        "can you sing a song": f"I know my creator Muskan loves singing, but I can't sing myself. Maybe you can, {user_name}!",
        "can you dance": f"I can't dance, but I bet you can, {user_name}.",
        "what is your favorite color": f"I don't have preferences, but I bet you'd like something vibrant, {user_name}!",
        "what is the biggest animal": "The blue whale is the largest animal on Earth.",
        "what is the smallest country": "The smallest country in the world is Vatican City.",
        "how far is the moon": "The moon is about 384,400 kilometers away from Earth.",
        "what is the tallest building": "The tallest building in the world is the Burj Khalifa in Dubai.",
        "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",
        "what is gravity": "Gravity is the force that pulls objects toward Earth.",
        "what is the meaning of life": f"The meaning of life is different for everyone. What's your take, {user_name}?",
        "who is albert einstein": "Albert Einstein was a famous physicist known for the theory of relativity.",
        "what is the periodic table": "The periodic table organizes all known chemical elements by their properties.",
        "can you tell me a quote": "Sure! 'Art enables us to find ourselves and lose ourselves at the same time.' - Thomas Merton",
        "who wrote harry potter": "Harry Potter was written by J.K. Rowling.",
        "what is a robot": "A robot is a machine that can perform complex tasks automatically."
    }

    while True:
        user_input = input(f"{user_name}: ").lower()

        # Look for exact matches in the dictionary
        if user_input in qa_pairs:
            print(f"Chatbot: {qa_pairs[user_input]}")
        
        # Farewell
        elif user_input in ["bye", "exit"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        
        # Default response
        else:
            print(f"Chatbot: I'm not sure how to respond to that, {user_name}.")
            
if __name__ == "__main__":
    chatbot()
