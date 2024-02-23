from typing import Annotated
from jwt import encode, decode
from deepdiff import DeepDiff


from fastapi import HTTPException, Header


ALGORITHM = "HS256"
JWT_SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
PAYLOAD = {"user": "name"}

def generate_token(userdata: dict) -> str:
    return encode(payload=PAYLOAD, 
                      key=JWT_SECRET_KEY, 
                      algorithm=ALGORITHM)


def verify_token(Authorization: Annotated[str, Header()]) -> bool:
    try:
        if not DeepDiff(PAYLOAD, decode(jwt=Authorization, key=JWT_SECRET_KEY, algorithms=ALGORITHM)):
            return True
        raise HTTPException(status_code=400, detail="Unauthorized")
     
    except Exception as ex:
        raise HTTPException(status_code=400, detail="Unauthorized")
