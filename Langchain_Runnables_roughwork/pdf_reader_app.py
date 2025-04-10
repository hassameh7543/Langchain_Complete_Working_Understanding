from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS              # Chroma is ko be use kyia ja saktha hai 
from langchain.llms import OpenAI


# Firstly load the document 
Loader = TextLoader("docx.txt")   # ensur the the docx.txt file exist in the system or in the directory
documents = Loader.load()

# Secondly split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Thirdly convert the text into embeddings $ store it in the FAISS

#  embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())


# Fourthly create the retriever (fetch reteriver documents)
retriver = vectorstore.as_retriever()  # yeha per ye reteriver ka kam kr raha hai jo kha like mutlab kha semantic search ka kam jo kha kr raha hai


# Manually reterive the revevant documents
query = "What is the sentiment of the following text? I love programming in Python!"
retrieved_docs = retriver.get_relevant_documents(query)

# combined the reterived text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in docs])


# instantiate the LLM 
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Manually pass Reterive the text into LLM
prompt = f"Based on the following text, what is the sentiment?: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

# print the answer
print("Answer :", answer)