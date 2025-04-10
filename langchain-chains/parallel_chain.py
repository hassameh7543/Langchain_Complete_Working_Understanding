from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI() # yeha per mara phela model hai jo kha openai sa chat krta hai

model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219') # or ye ma na second model use kyia hai jo kha quiz bna kha da da ja ye kuch be kam kra ja.

# phir yeha per ma na first promt bnaya through PromptTemplate
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

# Yeha per ma na second prompt use kyia through PromptTemplate
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)
# Yeha per ma na third prompt use kyia through PromptTemplate
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser() # then phir yeha per ma na parser use kyia hai 

parallel_chain = RunnableParallel({ # this is the parallel chain which is used to run the multiple chain at the same time.
    'notes': prompt1 | model1 | parser, # this is the first chain which is used to generate the notes from the text
    'quiz': prompt2 | model2 | parser   # this is the second chain which is used to generate the quiz from the text
})

merge_chain = prompt3 | model1 | parser # this is the merge chain which is used to merge the notes and quiz into a single document

chain = parallel_chain | merge_chain # this is the final chain which is used to run the parallel chain and then merge the notes and quiz into a single document

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text':text}) # this is used to invoke the chain which is used to run the chain and get the output.  

print(result)

chain.get_graph().print_ascii() # this is used to print the graph of the chain which is used to visualize the chain.
# Compare this snippet from langchain-core/prompts.py:

