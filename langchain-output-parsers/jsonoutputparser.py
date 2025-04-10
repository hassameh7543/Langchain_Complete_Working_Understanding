from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    #template='Give me the name, age and city of a fictional person \n {format_instructions}',
    #input_variables=[],
    
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser # ye sara kam khud kr raha hai like sare cheese khud he parse hoja rahe hai nothing chnaeg in this code 

result = chain.invoke({'topic':'black hole'})

print(result)


# # 
# propmt = template.format()

# result = propmt.invoke(prompt)

# print(result)

# final_result = parser.parse(result.content)
# print(final_result)
# print(type(final_result) # this will show the result of the final output in the datatype 
# print(final_result['name']) # this will show the output of the final result just the name of the output