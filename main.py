import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from colorlog import ColoredFormatter
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Define custom log levels
QUESTION_LOG_LEVEL = 25
RESPONSE_LOG_LEVEL = 26
logging.addLevelName(QUESTION_LOG_LEVEL, "QUESTION")
logging.addLevelName(RESPONSE_LOG_LEVEL, "RESPONSE")

# Setup logger
def setup_logger():
    logger = logging.getLogger('CalidadQuery')
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)s:%(name)s:%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'QUESTION': 'blue',
            'RESPONSE': 'purple',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

# Define constants
PERSIST_DIR = "./storage"

def create_or_load_index(persist_dir):
    if not os.path.exists(persist_dir):
        logger.info("Storage directory not found. Creating new index.")
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        logger.info("Storage directory found. Loading existing index.")
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
    return index

# Initialize FastAPI app
app = FastAPI()

index = create_or_load_index(PERSIST_DIR)
query_engine = index.as_query_engine()

# Define the request and response models
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    response: str

@app.post("/query", response_model=QueryResponse)
async def query_calidad(request: QueryRequest):
    question = request.question
    logger.log(QUESTION_LOG_LEVEL, f"Question: {question}")
    
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    response = query_engine.query(question)
    logger.log(RESPONSE_LOG_LEVEL, f"Response: {response}")
    
    return QueryResponse(response=response)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
