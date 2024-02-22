from fastapi import FastAPI, File, UploadFile, Response
from process import convert_las_to_ply
import shutil

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(
    "/image",
    responses={
        200: {
            "content": {"image/png": {}}
        }
    }, response_class=Response
)
def get_image():
    image_bytes: bytes = generate_cat_picture()
    # media_type here sets the media type of the actual response sent to the client.
    return Response(content=image_bytes, media_type="image/png")


def generate_cat_picture(file_path: str = "store/temp.png"):
    # This is just a placeholder, you would normally use a library like PIL to generate an image.
    with open(file_path, "rb") as f:
        return f.read()
    # return b"fake image"


@app.get("calc")
async def calc(a: int, b: int):
    # print(convert_las_to_ply("Khodhin_5.las", "Khodhin_5.ply"))
    return {"result": a + b}


@app.post('/files')
def get_file(file: UploadFile = File(...)):
    # accept only .las files
    # print(file)
    # print(file.filename.strip().split(".")[-1].lower())
    # print(file.filename.strip().split(".")[-1].lower() == "las")
    # print((file[0:4] == b'LASF') or (file.filename.strip().split(".")[-1].lower() == "las"))
    # print(file.filename.strip().split(".")[-1].lower())
    # print(file.filename.strip().split(".")[-1].lower() != "las")
    # print(file.filename.strip().split(".")[-1].lower() != "las")

    try:
        if file.filename.strip().split(".")[-1].lower() != "las":
            return {"error": "File is not a .las file."}
        else:
            with open(file.filename, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
                convert_las_to_ply(file, file.filename.strip().split(".")[0] + ".ply");
                return {
                    "filename": file.filename,
                    "content_type": file.content_type,
                    "file_path": file.filename.strip().split(".")[0] + ".ply"
                }
    except():
        return {"error": "File is not a .las file or is corrupted."}


@app.post("/signin/")
async def signin(email: str, password: str):
    if email == "admin" and password == "admin":
        # token encode with SHA256
        token = "token_seasand"
        encoded_token = token.encode('SHA256')
        return {
            "status": "success",
            "data": {"email": email, "token": encoded_token},
            "message": "Logged in successfully."
        }
    else:
        return {
            "status": "failed",
            "data": {"email": email, "password": password},
            "message": "Invalid email or password."

        }


@app.post("/signup/")
async def signup(name: str, email: str, password: str):
    if email != "" and len(password) >= 8 and name != "":
        # token encode with SHA256
        token = ""
        encoded_token = token.encode('SHA256')
        return {
            "status": "success",
            "data": {"email": email, "token": encoded_token},
            "message": "Account created successfully."
        }
    else:
        return {
            "status": "failed",
            "data": {"email": email, "password": password},
            "message": "Please fill in all the fields and make sure your password is at least 8 characters long."
        }
