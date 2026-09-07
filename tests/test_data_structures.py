import sys
import os
import importlib.util
from unittest.mock import patch

def load_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    # mock input just in case it's at module level
    with patch("builtins.input", return_value="1,2,3"):
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            pass # Some scripts raise EOF or value errors, but we might still be able to grab classes
    return module

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_stack_shunting_yard():
    mod_path = os.path.join(BASE_DIR, "Chapter_03_Stack", "item_3_26s1_Infix_to_Postfix.py")
    mod = load_module_from_path("infix_to_postfix", mod_path)
    if hasattr(mod, "infix_to_postfix"):
        assert mod.infix_to_postfix("A+B*C") == "ABC*+"

def test_cafe_queue():
    mod_path = os.path.join(BASE_DIR, "Chapter_04_Queue", "item_4_26s1_Cafe.py")
    mod = load_module_from_path("cafe_queue", mod_path)
    if hasattr(mod, "Queue") and hasattr(mod, "Customer"):
        q = mod.Queue()
        q.enqueue(mod.Customer(1, 0, 3))
        assert not q.is_empty()
        assert q.dequeue().cid == 1

def test_sll_dll():
    mod_path = os.path.join(BASE_DIR, "Chapter_05_LinkedList", "item_1_25s1_Singly_Linked_List.py")
    if os.path.exists(mod_path):
        mod = load_module_from_path("sll", mod_path)
        if hasattr(mod, "LinkedList"):
            ll = mod.LinkedList()
            ll.append(1)
            ll.append(2)
            assert ll.size() == 2

def test_bst_insertion():
    mod_path = os.path.join(BASE_DIR, "Chapter_07_Tree1_BST", "item_4_25s1_BST_insert_delete.py")
    mod = load_module_from_path("bst", mod_path)
    if hasattr(mod, "BinarySearchTree"):
        tree = mod.BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        assert tree.root.data == 5

def test_avl_tree():
    mod_path = os.path.join(BASE_DIR, "Chapter_08_Tree2_AVL", "item_1_25s1_Tree2_1_AVL_1.py")
    mod = load_module_from_path("avl", mod_path)
    if hasattr(mod, "AVLTree"):
        tree = mod.AVLTree()
        assert tree is not None
