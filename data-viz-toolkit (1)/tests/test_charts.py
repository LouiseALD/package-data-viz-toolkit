import unittest
from src.data_viz_toolkit.charts import create_bar_chart

class TestCharts(unittest.TestCase):
    def test_create_bar_chart(self):
        data = {'A': 10, 'B': 20}
        self.assertIsNone(create_bar_chart(data))
