import re
import json

class RegistrationAssistant:
    def __init__(self):
        self.user_data = {}
        self.step = "greeting"

    def get_response(self, user_input):
        if self.step == "greeting":
            self.step = "name"
            return "Hello! Welcome to Free Online AI & Data Science Internship at Data Alcott Systems. I am your AI Registration Assistant. Let's start your registration.\nWhat is your full name?"

        elif self.step == "name":
            self.user_data['name'] = user_input.strip()
            self.step = "email"
            return f"Nice to meet you, {self.user_data['name']}! Please provide your email address."

        elif self.step == "email":
            email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', user_input)
            if email_match:
                self.user_data['email'] = email_match.group()
                self.step = "field"
                return f"Thanks! Email {self.user_data['email']} saved. What is your field of study? e.g., Computer Science"
            return "Please enter a valid email like name@gmail.com"

        elif self.step == "field":
            self.user_data['field'] = user_input.strip()
            self.step = "experience"
            return f"Great! Field: {self.user_data['field']}. Tell me about your programming experience? e.g., Beginner"

        elif self.step == "experience":
            self.user_data['experience'] = user_input.strip()
            self.step = "done"
            with open('registrations.json', 'w') as f:
                json.dump(self.user_data, f, indent=4)
            return f"Perfect! Registration Complete\nName: {self.user_data['name']}\nEmail: {self.user_data['email']}\nField: {self.user_data['field']}\nExperience: {self.user_data['experience']}\n\nThank you for registering!"

        else:
            return "Registration already completed. Type quit to exit."

assistant = RegistrationAssistant()
print("AI Registration Assistant Started. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit','exit','bye']:
        break
    response = assistant.get_response(user_input)
    print(f"Assistant: {response}") 