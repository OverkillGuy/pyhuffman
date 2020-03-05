import pytest
from pyhuffman import huffman

def test_func_ok():
    assert huffman.some_func() == 2, "Bad funccall"
