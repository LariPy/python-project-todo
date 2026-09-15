import os
import json
from datetime import datetime

DATA_FILE = "data.json"

def create_task(description: str):
    
    # data = []

    # open data.json
    # (move this later so that it's opened once when app is opened)
    # if os.path.exists(DATA_FILE):
    #     with open(DATA_FILE, "r", encoding="utf-8") as file:
    #         try:
    #             data = json.load(file)
    #         except json.JSONDecodeError:
    #             data = []

    # save task to data.json
    # with open(DATA_FILE, "w", encoding="utf-8") as file:
    #     json.dump(tasks, file)
    return


if __name__=="__main__":
    # test
    description = "wash dishes"
    create_task(description)

# TODO
# receive data
# open tasks.json (if it exists) (note2: open json when app is opened)
# edit opened data with new received data
# put data back to tasks.json with the edits
# 
# json.load, json.dump
# 
# check validations?
# - whether certain data is valid
#
# format:
# - task number (global variable counter?)
# - description
# - date added
# - due date
# - status (if completed: true/false)
# 
# json format is a list of dicts
# [
#   {
#   "key": "value"
#   }
# ].

# consider something othre than json
# maybe sqlite
# could first make json then later learn sqlite