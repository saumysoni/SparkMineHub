from transformers import pipeline
import torch
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import chainlit as cl

# model and tokenizer loading
checkpoint = "LaMini-Flan-T5-783M"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
base_model = AutoModelForSeq2SeqLM.from_pretrained(
    checkpoint, 
    torch_dtype=torch.float32)


#@st.cache_resource
def llm_pipeline():
    pipe = pipeline(
        'text2text-generation',
        model=base_model,
        tokenizer=tokenizer,
        max_length=2048,
        do_sample=False,
        temperature=0.01,
        top_p=0.99
    )
    local_llm = HuggingFacePipeline(pipeline=pipe)
    return local_llm


#@st.cache_resource
def qa_llm():
    llm = llm_pipeline()
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="db", embedding_function=embeddings)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    return qa


import re

def remove_redundant_sentences(text):
    # Use regex to split text on punctuation while keeping it ('.', '!', '?')
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())  
    
    seen = set()
    cleaned_sentences = []
    
    for sentence in sentences:
        cleaned_sentence = sentence.strip().lower()  # Strip whitespace and lowercase the sentence for comparison
        if cleaned_sentence not in seen:
            cleaned_sentences.append(sentence.strip())  # Keep the original sentence structure
            seen.add(cleaned_sentence)
    
    return '. '.join(cleaned_sentences)  # Join sentences back with periods

def process_answer(instruction):
    qa = qa_llm()
    generated_text = qa(instruction)
    answer = remove_redundant_sentences(generated_text['result'])
    
    return answer, generated_text

@cl.on_chat_start
async def start():
    chain = qa_llm()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to Minehub. What is your query?"
    await msg.update()

    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain") 
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["result"]

    await cl.Message(content=answer).send()


