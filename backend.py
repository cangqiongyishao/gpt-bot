from openai import OpenAI
import os
class Chatbot:
    def __init__(self):
        GPT_API=os.getenv('GPTAPI')
        self.client=OpenAI(api_key=GPT_API)

    def get_response(self,user_input):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )

        return response.choices[0].message.content

if __name__=='__main__':
    chatbot=Chatbot()
    response=chatbot.get_response('Write a joke about birds.')

