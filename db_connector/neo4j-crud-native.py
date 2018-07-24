import json, datetime
import sys,os
from neo4j.v1 import basic_auth, GraphDatabase
os.path.join("../config/config.json")

class neo4j_crud:
    def __init__(self, *args, **kwargs):
        #config = json.loads(open("./config/config.json").read())
        config = json.load(open("../config/config.json"))
        username, password = config["username"], config["password"]
        url = "bolt://localhost:7687"
        self.driver= GraphDatabase.driver(url,auth=basic_auth(username,password))

    def close(self):
        self.driver.close()

    def add_nodes(self):
        with self.driver.session() as session:
            pass
            # Todo
   
    def read_nodes(self,tx):
        for records in tx.run("MATCH (n) RETURN n "):
            print(records)


if __name__=="__main__":
    db= neo4j_crud()
    with db.driver.session() as session:
        session.read_transactions(db.read_nodes)