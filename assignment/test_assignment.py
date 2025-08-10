from gradescope_utils.autograder_utils.decorators import weight
import unittest
import importlib
# import assignment
# import subdir1
# importlib.reload(assignment)

# This makes the import statements in assignment.py import into the current namespace.
exec(open('assignment/assignment.py').read())


class TestImport(unittest.TestCase):
    @weight(1)
    def test_import_1(self):
        """_summary_ Tests that add was not imported into the global namespace
        """
        try:
            add(2, 2)
        except Exception:
            pass  # Test passes if any exception is raised
        else:
            self.fail("Expected an exception to be raised")

    @weight(1)
    def test_import_2(self):
        """_summary_ Test that add was properly imported into the module namespace.
        """
        result = subdir1.subdir2.file3.add(2,2)
        self.assertEqual(result, 4)

    @weight(1)
    def test_import_3(self):
        result = ssf3.add(2,2)
        self.assertEqual(result, 4)

    @weight(1)
    def test_import_4(self):
        result = divide(4,2)
        self.assertEqual(result, 2)

    @weight(1)
    def test_import_5(self):
        self.assertEqual(oh_my, "Oh my!")
