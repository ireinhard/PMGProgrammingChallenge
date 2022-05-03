import unittest
import csvCombiner
import pandas as pd

class TestCombiner(unittest.TestCase):
    def test_combiner_success(self):
        actual = csvCombiner.makeCombinedCSV(['./fixtures/clothing.csv'], 50000)
        expected = pd.read_csv('./fixtures/clothing.csv')
        actualRow0 = len(actual.iloc[0])
        expectedRow0 = len(expected.iloc[0])
        # Should not be equal as didn't add new column
        self.assertNotEqual(actualRow0, expectedRow0)