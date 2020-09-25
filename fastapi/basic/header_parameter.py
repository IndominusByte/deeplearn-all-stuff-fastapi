"""
Header has a little extra functionality on top of what Path, Query and Cookie provide.

Most of the standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).

But a variable like user-agent is invalid in Python.

So, by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.

Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").

So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar.

If for some reason you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False:
"""
from fastapi import FastAPI, Header
from typing import Optional, List

app = FastAPI()

@app.get('/items')
def read_items(user_agent: str = Header(...)):
    return {"User-Agent": user_agent}


# Duplicate headers
"""
If you communicate with that path operation sending two HTTP headers like:

X-Token: foo
X-Token: bar

The response would be like:
{
    "X-Token values": [
        "bar",
        "foo"
    ]
}
"""
@app.get("/tokens")
async def read_tokens(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}
