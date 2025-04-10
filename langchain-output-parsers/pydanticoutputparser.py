from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field # jb hum pydantic use krtay hayein to hum na is libraries ko use krna hota hai 
# from langchain .output_parsers # ctrl duba kha pta lg saktha hai kha kitnay [arser or be hayien humaray pas ]

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# ab hum na  pydantic object hai jo kha schema ka kam kr ja or wo ye neechay bana hoi hai 
class Person(BaseModel): # yeha sa humara main kam start hota hai pydantic_outpt_parser  ka 

    # ye jitne he cheesenay hayein ye sare attributes hai jo ke humne define kiya hai
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person) # then yeha per ma na ak parser ko use kyia ahi jo kha pydantic output parser ko use kr raha hai 

# yeha per ab humay ak prompt likhan hai jo kha PromptTemplate use kra ja 
template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# ab yeha per hum apna prompt perform kray gay  jo kha kuch is tarah hai
# prompt = template.invoke({'place':'sri lankan'})
# ab is sa humay ak result milay ja or us ko hum parser kha pas bage dyien gay let seee with an help of code

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result) 

chain = template | model | parser

final_result = chain.invoke({'place':'sri lankan'})

print(final_result)
