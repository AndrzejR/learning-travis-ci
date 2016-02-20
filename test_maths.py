import maths, unittest

class TestMaths(unittest.TestCase):

	def test_add(self):
		self.assertEqual(maths.add(1,2),3)
		self.assertFalse(maths.add(1,2)==4)
		self.assertTrue(maths.add(2,2)==4)

	def test_multiply(self):
		self.assertEqual(maths.multiply(4,4),16)
		self.assertFalse(maths.multiply(1,2)==16)
		self.assertTrue(maths.multiply(2,2)==4)
