from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate
import openai
import os

import PyPDF2
from PyPDF2 import PdfReader

#  temperature=0 This means that the language model will be less likely to generate creative or unexpected text

llm = OpenAI(temperature=0, openai_api_key = "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")

def summary(essay):

    llm.get_num_tokens(essay)

    #split txte to chunk 
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500)
   
    #put all chunk in document
    docs = text_splitter.create_documents([essay])
    num_docs = len(docs)

    num_tokens_first_doc = llm.get_num_tokens(docs[0].page_content)

    # make the first prompt to summary each chunk 
    map_prompt = """
    You are a helperful research assistant Write a concise summary of the following research:
    "{text}"
    CONCISE SUMMARY:
    """
    map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])

    # make the second prompt to combine summary of each chunk and generate last summary
    combine_prompt = """
    You are a helperful research assistant Write a concise summary of the following text delimited by triple backquotes.
    Return your response in bullet points which covers the key points of the text gave the summary in same language of txte and in some details.
    ```{text}```
    BULLET POINT SUMMARY:
    """
    combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])

    summary_chain = load_summarize_chain(llm=llm,
                                        chain_type='map_reduce',
                                        map_prompt=map_prompt_template,
                                        combine_prompt=combine_prompt_template,
    #                                      verbose=True
                                        )
    output = summary_chain.run(docs)
    return str(output)