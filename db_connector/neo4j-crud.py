import json, datetime
import sys
from neo4j.v1 import basic_auth, GraphDatabase

class neo4j_crud:
    def __init__(self, *args, **kwargs):
        config = json.loads(open("./config/config.json").read())
        username, password = config["username"], config["password"]
        url = "bolt://localhost:7687"
        self.driver= GraphDatabase.driver(url,auth=basic_auth(username,password))

if __name__=="__main__":
    db= neo4j_crud()