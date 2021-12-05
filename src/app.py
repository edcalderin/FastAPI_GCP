from fastapi import FastAPI

app = FastAPI()

@app.get('/api')
def get_message():
    return {'message':'Hello world'}