from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def main():
    embedding = HuggingFaceEmbeddings()
    db = Chroma(persist_directory='./chroma_db', embedding_function=embedding)
    prompt = "Does this plan cover dental services"

    results = db._similarity_search_with_relevance_scores(prompt, k=4)

    context_text = "\n\n--\n\n".join([doc.page_content for doc, score in results])
    print(context_text)

    PROMPT_TEMPLATE = """
        Answer the following question based on the following context:
        {context}

        Answer the question based on the context above: 
        {prompt}
    """

    

main()