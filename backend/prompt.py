from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

def ask_prompt(prompt: str, file_name: str) -> str:
    embedding = HuggingFaceEmbeddings()

    # load vector store
    db = Chroma(persist_directory='backend/chroma_db', embedding_function=embedding)
    retreiver = db.as_retriever(search_type="mmr", search_kwargs={'k': 5, 'fetch_k': 5, 'filter': {'filename': {"$eq": file_name}}})
    
    # get associated chunks and format structure
    results = retreiver.invoke(prompt)
    context_text = "\n  --\n".join([doc.page_content for doc in results])
    sources = [doc.metadata['filename'] for doc in results]
    
    # prompt template to be given to llm
    PROMPT_TEMPLATE = """
        Answer the following question based on the following context:
        {context}

        Answer the question based on the context above: 
        {question}
    """

    prompt_serve = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt_serve | llm | StrOutputParser()
    response = chain.invoke({"context": context_text, "question": prompt})
    print_all = f"Response: {response} \nSources: {sources}"
    print(print_all)
    return response


