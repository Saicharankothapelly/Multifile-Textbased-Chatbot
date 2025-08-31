### knowledgebase-multi-file-chatbot

📚 Knowledge Base Multifile Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for querying multiple file formats (PDF, DOCX, Excel, DXF, DWG) in a knowledge base.
The chatbot leverages LangChain, Chroma vector database, and HuggingFace/OpenAI embeddings to answer questions based on your uploaded documents.


### 🌟 Features

Supports PDF, DOCX, Excel, CSV, DXF, and DWG files.

Automatically extracts text from documents and splits into semantic chunks.

Generates embeddings using HuggingFace all-mpnet-base-v2 model.

Stores embeddings in Chroma vector store for fast retrieval.

Uses OpenAI GPT or HuggingFace LLMs for generating precise answers.

RAG setup ensures accurate, context-based answers, reducing hallucinations.


### 🛠 Tech Stack

Python 3.10+

LangChain – chains, prompts, retrieval, document processing

Chroma – vector database for semantic search

HuggingFace Embeddings – semantic embeddings

OpenAI GPT – large language model for responses

PDFPlumber, python-docx, pandas, ezdxf – document parsing

DWG → DXF conversion using ODAFileConverter


### 📂 Project Structure
.
├── main.py                 # Entry point for chatbot
├── rag_chain.py            # RAG chain creation
├── chatbot.py              # LLM & embedding model initialization
├── file_loader.py          # Load and parse multiple file formats
├── knowledge_base/         # Folder containing your PDF/DOCX/Excel/CSV files
├── chroma_db/              # Persisted vector database (auto-generated)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

### ⚡ Setup Instructions

Python 3.8 or higher

Git – Download Git

- **Hugging Face API Token** – [Get your token here](https://huggingface.co/settings/tokens)

- **OpenAI API Key** (optional, if using OpenAI LLM) – [Get your API key](https://platform.openai.com/account/api-keys)

- **ODA File Converter** (Handle DWG files) – [Download ODAFileConverter](https://www.opendesign.com/guestfiles/oda_file_converter)


### setup project in your system

#####  step 1
git clone https://github.com/Saicharankothapelly/knowledgebase-multi-file-chatbot.git
cd pdf-kb-chatbot

##### step 2
create a virtual environment
python -m venv kb-mf-cb

activate environment
###### Windows
kb-mf-cb\Scripts\activate
###### macOS/Linux
source kb-mf-cb/bin/activate

##### step 3

install all the dependencies 

pip install -r requirements.txt

##### step 4

Set environment variables

create a .env file in your project directory 

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
OPENAI_API_KEY=your_openai_api_key  # optional if using OpenAI LLM


### How to get Hugging Face API Token:

Go to hugging face https://huggingface.co/settings/tokens

Click Access Tokens → +Create new token

Choose read access, name your token, and create it

Copy it into your .env file


##### Step 5

Add your Documents to Knowledge Base

Place your PDFs, DOCX, Excel, DWG, or DXF files in the knowledge_base/ folder.

##### Step 6 

Replace the KNOWLEDGE_BASE_DIR = 'with oue knowlege base path in your project derectory text_from_kb.py

##### Step 7 

Replace the ODA File convertor path in file_loader.py (you can find in C:\Program Files) after successfull installation.

##### Step 4 Run the ChatBot

python maiin.py 


##### Step 5

Chat with Bot 

Type your questions, and the bot will respond based on your knowledge base.

Type exit to quit.

##### ⚠ Common Issues & Fixes

HUGGINGFACEHUB_API_TOKEN not found
Cause: Environment variable missing
Solution: Add a .env file with HUGGINGFACEHUB_API_TOKEN

ImportError: No module named 'pdfplumber'
Cause: Dependency not installed or any forgotten to put in requirements.txt
Solution: Run pip install pdfplumber

DWG files not loading
Cause: ODAFileConverter path wrong or not installed
Solution: Install ODAFileConverter and update the path in convert_dwg_to_dxf() function

MemoryError / slow embeddings
Cause: Large knowledge base or high chunk size
Solution: Reduce chunk_size in RecursiveCharacterTextSplitter

Chroma DB not persisting
Cause: Wrong path or missing permissions
Solution: Ensure persist_directory="chroma_db" exists and is writable



### Alternatives

#### LLM Alternatives

HuggingFace Chat Models: Mistral, Falcon, LLaMA-2

OpenAI GPT: GPT-4, GPT-3.5-turbo

Local/Open Source LLMs: ollama 

#### Vector Database Alternatives

FAISS (local, fast similarity search)

#### Embedding Model Alternatives

HuggingFace Transformers: all-MiniLM-L6-v2, all-mpnet-base-v2

OpenAI Embeddings: text-embedding-3-small, text-embedding-3-large

Other Embeddings: CLIP (text + image), FastText


### Increase accuracy and performance of chatbot

#### RAG Chain Tuning

Experiment with number of retrieved documents (k) in the retriever to balance speed and context coverage.

For highly domain-specific KBs, consider fine-tuning the LLM or using specialized embeddings.

#### try different system prompts

#### try different chunck_size, chunch_overlap

#### use small knowledge base for fast and better performance


#### Hardware Considerations

Use GPU for faster embeddings and LLM inference.

Increase RAM for large KBs to avoid MemoryErrors.

If running on CPU, consider using smaller models or reducing batch size.

#### try different embedding models and llms

#### Preprocess Knowledge Base

Clean and structure documents before adding them to the KB to reduce irrelevant or noisy text.

Avoid extremely long or very small chunks that may reduce retrieval relevance.

###Limitations 

#### use small knowlege base for better performance

#### DWG and DFX Files:

This chatbot extracts only text-based content from DXF/DWG files (TEXT and MTEXT entities).

Images, drawings, or non-text elements are ignored, so the bot cannot answer questions based on graphics.

DWG → DXF conversion relies on ODAFileConverter, and errors may occur if:

Files are corrupted or use unsupported AutoCAD versions.

The converter path is misconfigured.

For non-textual CAD content, consider using image-based OCR or CAD-specific AI tools.

Ensure that text in the CAD files is accurately positioned and readable, otherwise RAG retrieval may fail to provide relevant answers.