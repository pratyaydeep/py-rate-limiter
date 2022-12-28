from fastapi import FastAPI, Request

app = FastAPI()

vis = set()

@app.get("/")
async def root(request : Request):
    client_host = request.client.host
    if client_host in vis :
        return {"message": "Already logged in"}
    else:
        vis.add(client_host)
        return {"client_host":client_host} 
