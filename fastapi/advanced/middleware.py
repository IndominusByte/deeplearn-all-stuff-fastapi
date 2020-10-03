from fastapi import FastAPI

app = FastAPI()

# HTTPSRedirectMiddleware
# Any incoming requests to http or ws will be redirected to the secure scheme instead.

# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# app.add_middleware(HTTPSRedirectMiddleware)


# TrustedHostMiddleware
# Enforces that all incoming requests have a correctly set Host header, in order to guard against HTTP Host Header attacks.

# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["example.com","*.example.com"]
# )

# GZipMiddleware
# Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header.
# minimum_size - Do not GZip responses that are smaller than this minimum size in bytes. Defaults to 500.

from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get('/')
def main():
    return {"message":"hello world"}
