from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import shutil
from pathlib import Path
import os
from io import BytesIO
import zipfile

app = FastAPI()

@app.post("/upload/{username}/")
async def upload_file(username: str, file: UploadFile = File(...)):
    folder_path = f"files/{username}"
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    file_location = f"{folder_path}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@app.get("/images/{username}/")
async def get_images(username: str):
    folder_path = f"files/{username}"
    if not os.path.exists(folder_path):
        raise HTTPException(status_code=404, detail="User folder not found")

    zip_filename = f"{username}_images.zip"
    zip_io = BytesIO()
    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as temp_zip:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                temp_zip.write(os.path.join(root, file), arcname=file)
    zip_io.seek(0)

    return StreamingResponse(zip_io, media_type="application/x-zip-compressed", headers={"Content-Disposition": f"attachment; filename={zip_filename}"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")

