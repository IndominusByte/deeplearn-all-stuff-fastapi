"""
You can declare multiple File and Form parameters in a path operation, but you can't also declare Body fields that you expect to receive as JSON, as the request will have the body encoded using multipart/form-data instead of application/json.
"""
from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post('/files')
def create_file(file: bytes = File(...)):
    print(file)
    return {"file_size": len(file)}


"""
UploadFile has the following attributes:

- filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
- content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
- file: A SpooledTemporaryFile (a file-like object). This is the actual Python file that you can pass directly to other functions or libraries that expect a "file-like" object.

UploadFile has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

- write(data): Writes data (str or bytes) to the file.
- read(size): Reads size (int) bytes/characters of the file.
- seek(offset): Goes to the byte position offset (int) in the file.
    * E.g., await myfile.seek(0) would go to the start of the file.
    * This is especially useful if you run await myfile.read() once and then need to read the contents again.
- close(): Closes the file.
"""
@app.post('/uploadfiles')
async def create_uploadfiles(file: UploadFile = File(...)):
    size = await file.read()
    print(len(size))
    await file.close()
    return {"filename": file.filename}


# Multiple file uploads
# To use that, declare a List of bytes or UploadFile:
@app.post("/files2")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles2")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
