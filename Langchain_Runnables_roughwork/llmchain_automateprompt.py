from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


#  Load the document 
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

#  create the prompt template 
prompt_template = PromptTemplate(
    input_variables=["topic"],   # defne what the inut is needed
    template="What is the sentiment of the following text? {topic}"
)

# create an LLMChain 
chain = LLMChain(llm=llm, prompt=prompt_template)  # ye yeha per automatic prompt generate kyia hoi hai ma na

# run the chain with the specific topic 
topic = input('Enter a topic')
output = chain.run(topic)

print("Generated the Blog title:", output)
