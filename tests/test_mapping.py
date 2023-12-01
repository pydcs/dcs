import unittest
from dcs.mapping import Polygon, Point, Rectangle, Triangle
from dcs.terrain import Caucasus


class PointTests(unittest.TestCase):
    def test_point(self) -> None:
        terrain = Caucasus()

        p1 = Point(2, 2, terrain)
        p2 = p1 + Point(1, 1, terrain)

        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 3)

        p2 = 1 + p1
        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 3)

        self.assertEqual(3 * p2, Point(9, 9, terrain))

        self.assertEqual(p2.x, 3)
        self.assertEqual(p2.y, 3)

        self.assertEqual(p2 * 0.5, Point(1.5, 1.5, terrain))

        p2 = p1 - 1
        self.assertEqual(p2.x, 1)
        self.assertEqual(p2.y, 1)

        p2 = p1 - p2
        self.assertEqual(p2.x, 1)
        self.assertEqual(p2.y, 1)

    def test_latlng(self) -> None:
        terrain = Caucasus()
        p = Point(0, 0, terrain)
        ll = p.latlng()
        self.assertAlmostEqual(ll.lat, 45.129497060328966)
        self.assertAlmostEqual(ll.lng, 34.265515188456)

        p2 = Point.from_latlng(ll, terrain)
        self.assertAlmostEqual(p2.x, 0)
        self.assertAlmostEqual(p2.y, 0)

    def test_point_eq(self) -> None:
        terrain = Caucasus()
        self.assertEqual(Point(0, 0, terrain), Point(0, 0, terrain))
        self.assertNotEqual(Point(0, 0, terrain), Point(0, 1, terrain))
        self.assertNotEqual(Point(0, 0, terrain), Point(1, 0, terrain))
        self.assertNotEqual(Point(0, 0, terrain), None)


class RectangleTests(unittest.TestCase):
    def test_rectangle(self) -> None:
        terrain = Caucasus()
        r = Rectangle(0, 0, 10, 10, terrain)

        self.assertEqual(r.center(), Point(5, 5, terrain))

    def test_resize(self) -> None:
        terrain = Caucasus()
        r = Rectangle(0, 0, 10, 10, terrain)

        r2 = r.resize(0.5)
        self.assertEqual(r2, Rectangle(2.5, 2.5, 7.5, 7.5, terrain))

        r2 = r.resize(2)
        self.assertEqual(r2, Rectangle(-5, -5, 15, 15, terrain))

    def test_random_point(self) -> None:
        terrain = Caucasus()
        r = Rectangle(10, 0, 0, 10, terrain)

        for i in range(0, 100):
            rp = r.random_point()
            self.assertTrue(r.point_in_rect(rp))


class TriangleTests(unittest.TestCase):
    def test_triangle_random(self) -> None:
        terrain = Caucasus()
        t = Triangle((Point(0, 5, terrain), Point(1, 2, terrain), Point(3, 1, terrain)))
        self.assertIsNotNone(t)


class PolygonTests(unittest.TestCase):
    def test_poly_triangulation(self) -> None:
        terrain = Caucasus()
        points = [Point(1, 2, terrain),
                  Point(3, 1, terrain),
                  Point(7, 2, terrain),
                  Point(9, 4, terrain),
                  Point(6, 6, terrain),
                  Point(6, 9, terrain),
                  Point(4, 8, terrain),
                  Point(2, 9, terrain),
                  Point(1, 7, terrain),
                  Point(0, 5, terrain)]
        poly = Polygon(terrain, points)
        areas = [x.area() for x in poly.triangulate()]
        self.assertEqual(areas, [2.5, 9.5, 10.0, 7.5, 9.0, 1.0, 5.0, 0.0])

    def test_poly_random(self) -> None:
        terrain = Caucasus()
        points = [
            Point(1, 2, terrain),
            Point(3, 1, terrain),
            Point(7, 2, terrain),
            Point(9, 4, terrain),
            Point(6, 6, terrain),
            Point(6, 9, terrain),
            Point(4, 8, terrain),
            Point(2, 9, terrain),
            Point(1, 7, terrain),
            Point(0, 5, terrain)]
        poly = Polygon(terrain, points)

        for i in range(0, 100):
            rp = poly.random_point()
            self.assertTrue(poly.point_in_poly(rp))
