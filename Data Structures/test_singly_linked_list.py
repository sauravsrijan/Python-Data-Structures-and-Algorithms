import pytest

import singly_linked_list


def setup_function(function):
    global llist
    llist = singly_linked_list.LinkedList()

def test_append_len():
    """Doing llist.append(obj) should add obj at the end of the linked list."""
    assert len(llist) == 0
    objects = ('a', 1, object(), ['list'], ('tuple',), {0: 'dict'}, {'set'})
    for length,o in enumerate(objects, start=1):
        llist.append(o)
        assert len(llist) == length
        assert llist.tail.data == o

def test_str_repr():
    """Calling str() and repr() on a linked list should output the data in a tuple as a string."""
    assert str(llist) == '()'
    assert repr(llist) == '()'
    llist.append('a')
    llist.append(123)
    assert str(llist) == "('a', 123)"
    assert repr(llist) == "('a', 123)"

def test_getitem():
    """Given an integer, n, llist[n] should return the node at position n"""
    with pytest.raises(TypeError):
        llist['a']
    
    with pytest.raises(IndexError):
        llist[0]
    
    with pytest.raises(NotImplementedError):
        llist[:]
    
    for c in 'abcdefg': llist.append(c)
    
    assert llist[0].data == 'a'
    assert llist[1].data == 'b'

    assert llist[-1].data == 'g'
    assert llist[-3].data == 'e'
    assert len(llist) == len('abcdefg')

def test_setitem():
    """llist[n] == obj should insert obj at index n"""
    with pytest.raises(IndexError):
        llist[0] = 'new data'
    
    llist.append('a')
    
    with pytest.raises(TypeError):
        llist['a'] = 'new data'
    
    with pytest.raises(TypeError):
        llist[2:3] = 'new data'
    
    llist[0] = 'new data'

    assert len(llist) == 1
    assert llist[0].data == 'new data'

    for c in 'abc': llist.append(c)

    llist[1] = 'x'

    assert len(llist) == 4
    assert str(llist) == "('new data', 'x', 'b', 'c')"

    llist[-1] = 'tail'

    assert len(llist) == 4
    assert str(llist) == "('new data', 'x', 'b', 'tail')"

def test_prepend():
    """Doing llist.prepend(obj) should add a new node with data, obj, at the beginning of the linked list."""
    objects = ('a', 1, object(), ['list'], ('tuple',), {0: 'dict'}, {'set'})
    for length,o in enumerate(objects, start=1):
        llist.prepend(o)
        assert len(llist) == length
        assert llist.head.data == o

def test_append_at_node():
    """Doing llist.append_at_node(node, obj), should add a new node containing data, obj, after the given node."""
    for o in (1, 'a', [], {}, ()):
        with pytest.raises(TypeError):
            llist.append_at_node(o, 'DATA')
    
    outside_node = singly_linked_list.Node('new node data')    
    with pytest.raises(KeyError):
        llist.append_at_node(outside_node, 'New-er node data')
    
    for c in 'abc':
        llist.append(c)
    
    llist.append_at_node(llist[1], 'X')
    assert str(llist) == "('a', 'b', 'X', 'c')"

def test_insert_at_index():
    """Doing llist.insert_at_index(n) should insert a new node at the given index, n."""
    for c in 'abc': llist.append(c)
    
    with pytest.raises(TypeError):
        llist.insert_at_index('index', 'new data')
    
    with pytest.raises(ValueError):
        llist.insert_at_index(-2, 'new data')
    
    llist.insert_at_index(1, 'X')
    assert str(llist) == "('a', 'X', 'b', 'c')"

    llist.insert_at_index(400, 'tail')
    assert str(llist) == "('a', 'X', 'b', 'c', 'tail')"
    
    llist.insert_at_index(0, 'head')
    assert str(llist) == "('head', 'a', 'X', 'b', 'c', 'tail')"
    assert len(llist) == 6

def test_remove_node():
    """Doing llist.remove_node(data) should remove the first occurence of the node containing the given data."""
    with pytest.raises(ValueError):
        llist.remove_node('a')

    for c in 'abccd': llist.append(c)

    node_3 = llist[2]
    llist.remove_node('c')
    assert llist[2] != node_3
    assert len(llist) == len('abccd') - 1
    assert str(llist) == "('a', 'b', 'c', 'd')"
    
    with pytest.raises(ValueError):
        llist.remove_node('data')


def teardown_function(function):
    global llist
    del llist
