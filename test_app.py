import pytest
import json, requests
import models
import app

expected_response = [
	{
        "t_id": 1,
        "t_title": "tache_test",
        "t_description": "description_test",
        "t_done": False
    }
]

data = {
		'task': {"id": 1, "t_title": "title_test", "description": "desc_test", "done": False}
	}

url = 'http://125.0.0.1:5000'

mimetype = 'application/json'

headers = {
		'Content-Type': mimetype,
		'Accept': mimetype
	}

def test_db_init():
	"""Checks emptiness of BDD before tests"""
	assert requests.get(url) == []

def test_create_task():
	"""Creates a task that has et to be done and adds it to the BDD."""
	response = requests.post(url, json=json.dumps(data)) 
	assert response.content_type == 'application/json'
	assert app.TodoTaskList.get(app) == expected_response

def test_modify_task():
	"""Modifies the test task to mark it as done."""
	pass

def test_get_by_id():
	"""Gets the task from its id."""
	pass

def test_get_all():
	"""Get the complete list of tasks. There should be only one."""
	pass

def test_delete_task():
	pass