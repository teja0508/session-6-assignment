from enum import Flag
import pytest
import random
import string
import session6
import os
import inspect
import re
import time

README_CONTENT_CHECK_FOR = [
    'Nonlocal Scope',
    'Global Scope',
    'Local Scope'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5, 'proper formatting of README is required'


def test_session6_check_doc_string_len():
    #check more then 50 char
    f1 = session6.check_doc_string_len(session6.my_fibonacci)
    assert f1()==True, 'just do by character by character count'
   
    #less then 50
    f1 = session6.check_doc_string_len(test_function_name_had_cap_letter)
    assert f1()==False,'just do by character by character count'

def test_my_doc_string_outer_not_empty():
    assert session6.check_doc_string_len != "", "doc string can't be empty"

def test_my_doc_string_outer_exists():
    assert session6.check_doc_string_len.__doc__ is not None, "doc string can't be Type None"

def test_my_fibonacci():
    my_list = [1,2,3,5,8,13]
    f1 = session6.my_fibonacci()
    for i in my_list:
        assert i==f1(),'functionality not working as expected'

def test_add():
    assert session6.add(10, 20) == 30, "inncorrect addtion of two numbers"
	
def test_mul():
    assert session6.mult(10, 20,1) == 200, "incorrect multiplication of three numbers"
	
def test_div():
    assert session6.div(100, 4) == 25.0, "inncorrect division of two numbers"

def test_global_dictionary_variable_with_the_counts():

    mydict_val = {'add':4,'mult':3,'div':2}
    fn =session6.add
    value = session6.global_dictionary_variable_with_the_counts(fn)
    value(2,4),value(2,4),value(2,4),value(2,4),
    
    fn = session6.mult
    value = session6.global_dictionary_variable_with_the_counts(fn)
    value(1,2,3),value(1,2,3),value(1,2,3),
    fn = session6.div
    value = session6.global_dictionary_variable_with_the_counts(fn)
    value(2,4),value(2,4)
   
    assert session6.counters==mydict_val,'just count how many times each funtion is called..'

def test_check_docs_check_doc_string_len():
    assert bool(session6.check_doc_string_len.__doc__)==True,"Docstring missing"

def test_check_docs_my_fibonacci():
    assert bool(session6.my_fibonacci.__doc__)==True,"Docstring missing"

def test_check_docs_global_dictionary_variable_with_the_counts():
    assert bool(session6.global_dictionary_variable_with_the_counts.__doc__)==True,"Docstring missing"

def test_check_docs_add():
    assert bool(session6.add.__doc__)==True,"Docstring missing"


def test_check_docs_mult():
    assert bool(session6.mult.__doc__)==True,"Docstring missing"


def test_check_docs_div():
    assert bool(session6.div.__doc__)==True,"Docstring missing"
    
def test_closure_my_fibonacci():
    f1 = session6.my_fibonacci()
    assert bool(f1.__closure__)==True, 'Closure is missing'


def test_closure_check_doc_string_len():
    f1 = session6.check_doc_string_len(session6.my_fibonacci)
    assert bool(f1.__closure__)==True, 'Closure is missing'  

def test_closure_global_dictionary_variable_with_the_counts():
    fn = session6.add
    f1 = session6.global_dictionary_variable_with_the_counts(fn)
    assert bool(f1.__closure__)==True, 'Closure is missing'
    
def test_counter():
    c = dict()
    m = dict()
    d = dict()
    c_val, m_val, d_val = {'add':4},{'mult':3},{'div':2}
    fn = session6.add
    value =session6. counter(fn, c)
    value(1,2),value(1,2),value(1,2),value(1,2)
    fn = session6.mult
    value = session6.counter(fn, m)
    value(2,3,1),value(2,3,1),value(2,3,1)
    fn = session6.div
    value = session6.counter(fn, d)
    value(4, 2),value(4, 2)
    assert c == c_val,'just count how many times each funtion is called..'
    assert m == m_val,'just count how many times each funtion is called..'
    assert d == d_val,'just count how many times each funtion is called..'
