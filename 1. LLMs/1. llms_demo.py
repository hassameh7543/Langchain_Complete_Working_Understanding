from langchain_openai import OpenAI
from langchain import LangChain
import dotenv import load_dotenv
import os

load_dotenv()  # Frst we have to invok it and Now Ab humaray pas jo API Key ho je wo a gaye je

# gpt-3.5-turbo-instruct is the model name
llm = OpenAI(model='gpt-3.5-turbo-instruct')
# OpenAI is the class name and model is the parameter of the class and gpt-3.5-turbo-instruct is the value of the parameter and llm is the object of the class
# invoke is the method of the class and "What is the capital of India" is the parameter of the method
result = llm.invoke("What is the capital of India")
# invoke: it is the very important function in langchain that is responsible for generating the output of the model
# invoke: is particular function kha zyria sa hum apnay model sa bt krya gay
print(result)
