import os
import PyPDF2
import re
import openai

openai.api_key = ""




def translate(data):
    pdf_translate_text = ""
    
    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful translater assistant."},
                            {"role": "user", "content": f"translate this to Arabic: {data}"},
                                ],
                                    )
    txt_translate = response["choices"][0]["message"]["content"]
    pdf_translate_text+=txt_translate + "\n"

    return pdf_translate_text





