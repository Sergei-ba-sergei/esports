from fastapi import FastAPI
from src.PydanticModels.ProOrAmateur import Name
from src.get_amateur_names import get_some_amateurs
from src.get_player_prediction import get_player_prediction

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the best pro play predictor you've never seen"}

@app.get("/getPlayers/")
async def players():
    return     {"message": "Here are 10 players you may be interested in",
                "players": get_some_amateurs()}

@app.post("/ProOrAmateur/")
async def pro_or_amateur(name: Name):
    result = get_player_prediction(name.name)
    return result
