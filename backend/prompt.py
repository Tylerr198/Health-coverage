from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

def ask_prompt(prompt: str) -> str:
    embedding = HuggingFaceEmbeddings()

    # load vector store
    db = Chroma(persist_directory='./chroma_db', embedding_function=embedding)

    # get associated chunks and format structure
    results = db._similarity_search_with_relevance_scores(prompt, k=4)
    context_text = "\n  --\n".join([doc.page_content for doc, score in results])

    PROMPT_TEMPLATE = """
        Answer the following question based on the following context:
        {context}

        Answer the question based on the context above: 
        {question}
    """

    prompt_serve = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    chain = prompt_serve | llm | StrOutputParser()

    return chain.invoke({"context": context_text, "question": prompt})



