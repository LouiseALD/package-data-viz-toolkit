import unittest
from src.data_viz_toolkit.dashboards import create_dashboard

class TestDashboards(unittest.TestCase):
    def test_create_dashboard(self):
        data = {'A': 10, 'B': 20}
        # Test if dashboard creates without exceptions
        try:
            create_dashboard(data)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)
