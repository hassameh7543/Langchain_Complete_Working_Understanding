from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

# ye kam kuch is thera kra ja kha sb sa phelay prompt1 ak model kha pas gay ja then wo model humay kuch response generate kra ja then us ko hum phir parser kha pas bage dyien gay then wo humay detailed report humay da da ja ye is thea kam kra ja next promt kha lyia be same asay he kam ho ja 
chain = prompt1 | model | parser | prompt2 | model | parser # chain isey ko bola jata hai or is thera he hum chins ko bnatay hayien 

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

chain.get_graph().print_ascii()