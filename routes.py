from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


def extract_name(dwarf_dict):
    '''
    taking dictionary of dwarves and adding names to dictionary
    '''
    dwarf_name = {}
    name = []
    for dwarf_list in dwarf_dict["dwarves"]:
        name.append(dwarf_list["name"])
    dwarf_name["dwarves"] = name
    return dwarf_name

def extract_dwarf_info(dwarf_dict, name):
    '''
    taking dictionary of dwarves and name of dwarf to add details of dwarf to dictionary
    '''
    dwarf_inf = {}
    dwarf_inf["dwarf"] = {}
    for dwarf_list in dwarf_dict["dwarves"]:
        if name in dwarf_list["name"]:
            dwarf_inf["dwarf"] = dwarf_list            
    return dwarf_inf


@app.route('/api/dwarves', methods=['GET'])
def names():
    '''
    creates route for accessing list of dwarves as json object
    '''
    #can also create error handling based on status code from API request
    try:
        #try block makes request to end point, processes data as json and passes it to appropriate function
        r = requests.get("https://thedwarves.pusherplatform.io/api/dwarves")
        requests_value = r.json()
        final_value = jsonify(extract_name(requests_value))
    except:
        #returns error json string if error with try block
        final_value = {"error": ""}
    return final_value

@app.route('/api/dwarves/<name>', methods=['GET'])
def dwarf_info(name):
    '''
    creates route for dwarf detail as json object
    '''
    #can also create error handling based on status code from API request
    try:
        #try block makes request to end point, processes data as json and passes it to appropriate function
        r = requests.get("https://thedwarves.pusherplatform.io/api/dwarves")
        requests_value = r.json()
        final_value = jsonify(extract_dwarf_info(requests_value, name))
    except:
        #returns error json string if error with try block
        final_value = {"error": ""}
    return final_value
