from pydantic import BaseModel

class POSTinfo(BaseModel):
  title :str
  content:str