from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    csv_file: str
