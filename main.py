from fastapi import FastAPI

import database
from queries import querie
from fastapi.middleware.cors import CORSMiddleware
import config

app = FastAPI(docs_url=config.documentation_url)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/produce")
def get_product():
    query = querie.produce
    produce = database.execute_sql_query(query)
    produce_to_return = []
    for produces in produce:
        produce_dictionary = {
                            "name": produces[0],
                            "picture": produces[1],
                            "paragraph": produces[2]
                            }
        produce_to_return.append(produce_dictionary)

    return {'produce': produce_to_return}

@app.get("/practice")
def get_practice():
    query = querie.practice
    practice = database.execute_sql_query(query)
    practice_to_return = []
    for practices in practice:
        practice_dictionary = {
                            "name": practices[0],
                            "picture": practices[1],
                            "paragraph": practices[2]
                            }
        practice_to_return.append(practice_dictionary)

    return {'practice': practice_to_return}
