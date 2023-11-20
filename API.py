import openai

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

respone = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    message=[
        {"role" : "user", "content" : "display odd numbers between 0 and 20 using the while loop"}
    ]
)

print(respone)