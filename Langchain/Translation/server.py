from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from fastapi import FastAPI

system_template = "Translate the following sentence to {language}"
user_template = "{sentence}"

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", user_template),
    ]
)
model = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()
chain = chat_prompt | model | parser

app = FastAPI()
add_routes(app, chain, path="/translate")

if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)