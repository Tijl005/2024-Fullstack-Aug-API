from fastapi import FastAPI
from models import models
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

@app.get("/tour_get")
def get_tour():
    query = querie.get_tour
    tour = database.execute_sql_query(query)
    tour_to_return = []
    for tours in tour:
        tour_dictionary = {
                            "tourId": tours[0],
                            "firstName": tours[1],
                            "lastName": tours[2],
                            "email": tours[3]
                            }
        tour_to_return.append(tour_dictionary)

    return {'tour': tour_to_return}

@app.post("/tour")
def create_tour(tour: models.tour):
    query = querie.insert_tour
    success = database.execute_sql_query(query,(
        tour.tourId,
        tour.firstName,
        tour.lastName,
        tour.email
    ))
    if success:
        return tour
