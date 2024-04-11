import os
from openai import OpenAI
import gradio as gr

from keys.third_part_api_keys import Constants


class OpenAi:
    def __init__(self) -> None:
        self.key = Constants.ThirdParty.OpenAi.KEY
        self.client = OpenAI(api_key=self.key)
        self.get_response = None

    def __call__(self):
        self.third_party_call()
        self.process_response()

    def third_party_call(self):
        pass

    def process_response(self):
        pass


# openai.api_key = "xxxxxx"

# start_sequence = "\nAI:"
# restart_sequence = "\nHuman: "

# prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

# def openai_create(prompt):

#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=prompt,
#     temperature=0.9,
#     max_tokens=150,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0.6,
#     stop=[" Human:", " AI:"]
#     )

#     return response.choices[0].text


# def chatgpt_clone(input, history):
#     history = history or []
#     s = list(sum(history, ()))
#     s.append(input)
#     inp = ' '.join(s)
#     output = openai_create(inp)
#     history.append((input, output))
#     return history, history


# block = gr.Blocks()


# with block:
#     gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>
#     """)
#     chatbot = gr.Chatbot()
#     message = gr.Textbox(placeholder=prompt)
#     state = gr.State()
#     submit = gr.Button("SEND")
#     submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

# block.launch(debug = True)
