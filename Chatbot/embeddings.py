from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from chromadb.config import Settings
import os
from constants import CHROMA_SETTING


def main():
    documents=[]
    for root,dirs,files in os.walk("docs"):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                loader = PDFMinerLoader(os.path.join(root,file))
    documents.extend(loader.load())
    text_splitter =RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    #create embeddings from the knowledge base here
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings, persist_directory="db")
    db.persist()

if __name__ == "__main__":
    main()