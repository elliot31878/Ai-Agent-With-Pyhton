
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
    model="llama3",
    base_url="http://localhost:11434"
)

template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews:
{reviews}

Here is the question to answer:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

result = chain.invoke({
    "reviews": "No reviews available.",
    "question": "What is the best pizza place in town?"
})

print(result.content)

