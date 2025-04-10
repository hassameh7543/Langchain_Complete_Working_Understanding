from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load OpenAI API key from environment variable
# Initialize the OpenAI LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# create the prompt template
# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="What is the sentiment of the following text? {topic}" #,{input}
)

# Define the input topic
topic = input("I love programming in Python!")

# format the prompt manually by using the prompt_template
                                          #topic=topic ye be use kr saktha hn ma neechay 
formatted_prompt = prompt_template.format(input=topic)

# Call the LLM to generate the sentiment
               # llm.predict be use kr saktha hn ma neechay 
response = llm.generate(formatted_prompt)

# Print the sentiment response
print("Generated the response:", response)
# Print the formatted prompt
print("Formatted Prompt:", formatted_prompt)
# Print the response from the LLM
print("Response:", response)