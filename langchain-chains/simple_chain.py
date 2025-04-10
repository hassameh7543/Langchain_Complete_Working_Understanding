from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

# Now we are creating a chain of components. The order of the components is important. like this : we have to first pass the prompt then model and then parser so that we can get the output.
chain = prompt | model | parser # Ye is thera kam kra ja kha jb ye prompt ko model ko or parser ko combine krta hai to ye ak chain banta hai jo kha humara output dy ja. 

result = chain.invoke({'topic':'cricket'}) # yeha per humay ak result milay ga jo kha humara output hoga

print(result)

# ye step humay chain kha ander kon kon sa step involve hoi hayien ye un ko humay show kra kha da da ja in the form of graph jis is hum is ko easliy visualize kr sakhay gay 
chain.get_graph().print_ascii() # yeha per humay ak graph milay ga jo kha humara chain ko represent krta hai