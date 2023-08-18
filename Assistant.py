import os
import PyPDF2
import re
import openai

openai.api_key = ""

def ask_assistant(data):
    Assistant_text = ""

    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": '''You are a helpful research  assistant.
                               I am a student who is writing a research paper .
                                I need your help to find relevant sources, summarize the key findings of these sources, and identify any language errors in my writing.'''},
                            {"role": "user", "content": f"answer this qusistuon if it is relate to scientific reseach: {data}"},
                                ],
                                    )
    txt_Assistant = response["choices"][0]["message"]["content"]
    Assistant_text+=txt_Assistant + "\n"

    return Assistant_text
