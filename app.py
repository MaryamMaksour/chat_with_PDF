from dotenv import load_dotenv

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
import qdrant_client
import os


def get_vector_store():
    client = qdrant_client.QdrantClient(
        os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY")
    )
    embeddings = OpenAIEmbeddings()

    vector_store = Qdrant(
        client=client,
        collection_name=os.getenv("QDRANT_COLLECTION"),
        embeddings=embeddings
    )

    return vector_store



def ask(data):
    load_dotenv()

    vector_store = get_vector_store() 

    qa = RetrievalQA.from_chain_type(
         llm=OpenAI(),
         chain_type="stuff",
         retriever=vector_store.as_retriever()
    )

    answer = qa.run(data)
    return answer
    

