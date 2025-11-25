from pydantic import BaseModel

class POSTinfo(BaseModel):
  title :str
  content:str

class POSTResponse(BaseModel):
  title :str
  content:str