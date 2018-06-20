import json, datetime
import sys
from neo4j.v1 import basic_auth, GraphDatabase
sys.path.append("../")
config = json.loads(open("../config/config.json").read())
username , password = config["username"], password["password"]
