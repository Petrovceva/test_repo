import pytest
from check_post import get_post, get_newpost

id_check = 91749
title_ = 'Monica'

def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
        print(item)
    assert id_check in res
    

def test_2():
    output = get_newpost()['data']
    res = []
    for item in output:
        res.append(item['title'])
        print(item)
    assert title_ in res
    
