import unittest
from wedding_data_processor import get_june_2024_weddings, get_upcoming_weddings,connect_to_db


class TestWeddingDataProcessor(unittest.TestCase):

    def setUp(self):
        self.conn = connect_to_db()  # 在每次测试前建立数据库连接

    def tearDown(self):
        self.conn.close()  # 测试完成后关闭数据库连接

    def test_june_2024_weddings(self):
        june_weddings = get_june_2024_weddings(self.conn)
        self.assertIsInstance(june_weddings, list)  # 确保返回的结果是一个列表

    def test_upcoming_weddings(self):
        upcoming_weddings = get_upcoming_weddings(self.conn)
        self.assertIsInstance(upcoming_weddings, list)  # 确保返回的结果是一个列表


if __name__ == "__main__":
    unittest.main()
