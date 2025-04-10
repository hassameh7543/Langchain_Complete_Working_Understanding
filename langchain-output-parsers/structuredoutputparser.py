from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'), # this is the main schema of the output.
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'), # this is how that we want to create the schema of the output
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema) # ye mara parser a schema hai jo kha structured_output_parser ko follow kr raha hai jo ke humne define kiya hai

# yeha per ma na prompt tayer kyia hai.
template = PromptTemplate(  # yeha hum is the template ko define kar rahe hai jo ke humne schema ke sath define kiya hai
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# chain = template | model | parser # yeha per hum chain ko define kar rahe hai jo ke humne template, model aur parser ko combine kar ke define kiya hai.

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content) # yeha per hum jo content use kr rahay hayein  besiaclly wo is wega sa kr rahay hayien q kha hum chain walay ke thera use kr rahay hayein.

# print(final_result)


chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)