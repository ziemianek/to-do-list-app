from project import * 
import pytest


def test_remove_task():
    add_task("test task", "today")
    
    assert remove_task(2) == False
    assert remove_task(1) == True
    assert remove_task(0) == False
    
def test_mark_task_as_completed():
    add_task("test task", "today")
    
    assert mark_task_as_completed(2) == False
    assert mark_task_as_completed(1) == True
    assert mark_task_as_completed(0) == False
    
def test_load_tasks():
    
    assert load_tasks("tasks.json") == True
    assert load_tasks("filename.json") == False
    assert load_tasks("filename") == False
    
