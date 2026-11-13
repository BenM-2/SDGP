
# from delivery.[folder_name].[sub-folder].[file] import *

from delivery.template_test.add import add 

def test_add():
    assert add(1,2) == 3 
