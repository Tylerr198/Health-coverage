from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

def main():

    embedding = HuggingFaceEmbeddings()

    # load vector store
    db = Chroma(persist_directory='./chroma_db', embedding_function=embedding)

    user_question = "Does this plan cover dental services"

    # get associated chunks and format structure
    results = db._similarity_search_with_relevance_scores(user_question, k=4)
    context_text = "\n  --\n".join([doc.page_content for doc, score in results])

    PROMPT_TEMPLATE = """
        Answer the following question based on the following context:
        {context}

        Answer the question based on the context above: 
        {question}
    """

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    chain = prompt | llm | StrOutputParser()

    print(chain.invoke({"context": context_text, "question": user_question}))

main()


