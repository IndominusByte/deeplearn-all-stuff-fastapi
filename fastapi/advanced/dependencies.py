"""
In Python there's a way to make an instance of a class a "callable".

Not the class itself (which is already a callable), but an instance of that class.

To do that, we declare a method __call__:
"""
from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()

class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: Optional[str] = None):
        if q:
            return q in self.fixed_content
        return False


checker = FixedContentQueryChecker("bar")

@app.get('/query-check')
def query_checker(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}
