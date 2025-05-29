## FastAPI Notes


### FastAPI Headers Example

```py
@app.get("/get-headers", status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent

    return request_headers
```