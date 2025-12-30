from pydantic import BaseModel


class RequestPrompt(BaseModel):
    prompt : str