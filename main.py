
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

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


while True:
    print("\n\n--------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    

    reviews = retriever.invoke(question)    
    result = chain.invoke({
        "reviews": reviews,
        "question": question
    })

    print(result.content)

