import openai
import gradio 


# openai.api_key = "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"
#
# messages = [{"role": "system", "content": "You know information on consumer computer specs that are sold online"}]
#
# def CustomChatGPT(user_input):
#     messages.append({"role":"user","content": user_input})
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = messages
#     )
#     ChatGPT_reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": ChatGPT_reply})
#     return ChatGPT_reply
#
# demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Tech Deals")
#
# demo.launch()


# import openai
# import gradio as gr
#
# openai.api_key = "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"  # Replace with your key

# def predict(message, history):
#     history_openai_format = []
#     for human, assistant in history:
#         history_openai_format.append({"role": "user", "content": human })
#         history_openai_format.append({"role": "assistant", "content":assistant})
#     history_openai_format.append({"role": "user", "content": message})
#
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages= history_openai_format,
#         temperature=1.0,
#         stream=True
#     )
#
#     partial_message = ""
#     for chunk in response:
#         if len(chunk['choices'][0]['delta']) != 0:
#             partial_message = partial_message + chunk['choices'][0]['delta']['content']
#             yield partial_message
#
# gr.ChatInterface(predict).queue().launch()

# The api key will be different because of reasons, but this key is how we will access the chatbot, be sure not the post the key in the github. 
#openai.api_key = "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"



def CustomChatGPT(user_input, history):
    messages = []
    for user, chatbot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": chatbot})
    messages.append({"role": "user","content": user_input})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1.0,
        stream = True
    )

    ChatGPT_reply = ""
    for chatresponse in response:
        if len(chatresponse['choices'][0]['delta']) !=0:
            ChatGPT_reply = ChatGPT_reply + chatresponse['choices'][0]['delta']['content']
            yield ChatGPT_reply

demo = gradio.ChatInterface(CustomChatGPT, title = "TEchCart")

demo.queue().launch()
