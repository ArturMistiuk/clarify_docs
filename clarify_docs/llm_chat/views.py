from PyPDF2 import PdfReader

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import openai

openai.api_key = "#"
CHUNK_SIZE = 1024
CHUNK_OVERLAP = 200
MAX_LEN = 512
TEMPERATURE = 0.5

# def get_completion(prompt):
#     print(prompt)
#     query = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=512,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#
#     response = query.choices[0].text
#     print(response)
#     return response


def query_view(request):

    if request.method == 'POST':
        prompt = request.POST.get('prompt')

        # user_question = request.POST.get('user_question')
        selected_pdf = request.POST.get('pdf_content')
        # selected_pdf = get_object_or_404(PDFDocument, id=selected_pdf_id)
        text_chunks = get_text_chunks(selected_pdf)

        knowledge_base = get_vectorstore(text_chunks)
        conversation_chain = get_conversation_chain(knowledge_base)

        chat_response = conversation_chain({'question': prompt})

        response = chat_response["answer"]




        # response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'llm_chat/index.html')


def index(request):
    pdf_content = None

    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']

        # Process the PDF content
        pdf_content = process_pdf(pdf_file)

    return render(request, 'index.html', {'pdf_content': pdf_content})


def process_pdf(pdf_file):
    pdf_text = ''
    try:
        # Read the uploaded PDF file
        pdf = PdfReader(pdf_file)

        # Extract text from each page
        for page in pdf.pages:
            pdf_text += page.extract_text()
    except Exception as e:
        pdf_text = f"Error processing PDF: {str(e)}"

    return pdf_text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        # separator="\n",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embeddings, persist_directory="vectorstore")
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id=LLM_MODEL, model_kwargs={"temperature": TEMPERATURE, "max_length": MAX_LEN})
    # llm = CTransformers(model='llama-2-7b-chat.Q4_K_M.gguf',
    #                     model_type='llama',
    #                     temperature=0.75,
    #                     max_tokens=2000,
    #                     top_p=1,
    #                     verbose=True,  # Verbose is required to pass to the callback manager
    #                     )
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
