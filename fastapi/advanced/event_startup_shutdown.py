from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def startup_event():
    print("web is up")

@app.on_event("shutdown")
def shutdown_event():
    print("web is shutting down")
