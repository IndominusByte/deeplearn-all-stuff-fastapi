from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.post('/files')
def create_files(
    file: bytes = File(...),
    file_upload: UploadFile = File(...),
    token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": file_upload.filename,
    }
