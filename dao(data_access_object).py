#DAO
#David Sanchez
#Ficha: 2502640

#Definition
""" Data Access Object (DAO), el cual permite separar la lógica de acceso a datos de los Objetos de negocios (Bussines Objects), de tal forma que el DAO encapsula toda la lógica de acceso de datos al resto de la aplicación. """

#Example
from flask import request, jsonify
from models import Anime, Sub_Group
from config import Config
import utils
from app import app, db, q
from models import Anime, DAO
from anidb import AniDB
import tasks
import json


@app.route("/")
def hello_world():
    # return angular js?
    return "Hello world"


@app.route("/api/search/anime")
def search_animes():
    """
    Search the databse for animes with the url
    /api/search/animes?search_term=somthig...
    """
    param_key = "search_term"
    search_term = request.args[param_key]
    dao = DAO(db.session)
    try:
        result = dao.search_anime(search_term)
        if len(result) == 0:
            return ("", 404, [])
        else:
            # this will need fixing
            app.logger.debug("found %s", len(result))
            return jsonify(json_list=[e.serialize() for e in result])
    except Exception as e:
        app.logger.exception(e)
        return (str(e), 500, [])
    finally:
        db.session.close()

    anime = Anime("one", "two", "three", "four")
    return jsonify(**utils.to_dict(anime))