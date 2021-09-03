import ast
import sys
import pytest
from python_minifobf import unparse
from python_minifobf.ast_compare import compare_ast

def test_fstring_empty_str():
    if sys.version_info < (3, 6):
        pytest.skip('f-string expressions not allowed in python < 3.6')

    source = r'''
f"""\
{fg_br}"""
'''

    print(source)
    expected_ast = ast.parse(source)
    actual_ast = unparse(expected_ast)
    compare_ast(expected_ast, ast.parse(actual_ast))
