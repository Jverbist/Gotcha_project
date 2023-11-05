# This a gotcha game made by me, it is a simple game with a simple concept.
from fastapi import FastAPI




# Import all the required libraries:
app = FastAPI()





# app code starts here:















# app gets executed here:

@app.get("/")
async def root():
    return {"message": "Hello World"}


# app posts execution code here:







