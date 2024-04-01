import debugpy
# Enable the debugger to listen on port 5678
debugpy.listen(('0.0.0.0', 5679))
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/test")
def test_api():
    return {"key": "some data"}
