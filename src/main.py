from fastapi import FastAPI

app = FastAPI(title="RAG v0", version="0.1")

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.1"}
