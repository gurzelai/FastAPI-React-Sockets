from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
import uvicorn
import asyncio

app = FastAPI()

class Machine(BaseModel):
    name: str
    value: float

machines: List[Machine] = []
websockets: List[WebSocket] = []

@app.post("/machines/")
async def crear_machine(machine: Machine):
    machines.append(machine)
    
    asyncio.create_task(notificar_websockets()) # Notify all active WebSockets in the background without waiting for this function to finish.
    # await notificar_websockets() # Notify all active WebSockets in the background by waiting for this function to finish.
    
    return machine

@app.get("/machines/", response_model=List[Machine])
async def obtener_machines():
    return machines

@app.websocket("/ws/machines")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websockets.append(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except WebSocketDisconnect:
        websockets.remove(websocket)

async def notificar_websockets():
    machines_dict = [machine.model_dump() for machine in machines]
    for websocket in websockets:
        try:
            await websocket.send_json(machines_dict)
        except Exception as e:
            print(f"Error sending data to WebSocket: {e}")
            websockets.remove(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
