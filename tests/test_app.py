import unittest

from app import app


class ShopLiteTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_shows_all_products(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"12 items", response.data)
        self.assertIn(b"Everyday Backpack", response.data)
        self.assertIn(b"Wireless Headphones", response.data)

    def test_search_is_case_insensitive(self):
        response = self.client.get("/?q=HEADPHONES")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Wireless Headphones", response.data)
        self.assertNotIn(b"Everyday Backpack", response.data)

    def test_category_filter_shows_matching_products(self):
        response = self.client.get("/?category=Accessories")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Everyday Backpack", response.data)
        self.assertIn(b"Steel Water Bottle", response.data)
        self.assertNotIn(b"Wireless Headphones", response.data)

    def test_search_and_category_can_be_combined(self):
        response = self.client.get("/?q=water&category=Accessories")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Steel Water Bottle", response.data)
        self.assertNotIn(b"Everyday Backpack", response.data)

    def test_no_matches_shows_helpful_message(self):
        response = self.client.get("/?q=not-a-product")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"No products found", response.data)

    def test_adding_product_still_works_with_filters(self):
        response = self.client.post("/cart/add/1")

        self.assertEqual(response.status_code, 302)
        cart_response = self.client.get("/cart")
        self.assertIn(b"Everyday Backpack", cart_response.data)


if __name__ == "__main__":
    unittest.main()
