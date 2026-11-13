"""Unit tests using synthetic values only."""

import unittest

from crash_rate import crash_rate_per_million_vmt


class CrashRateTests(unittest.TestCase):
    def test_synthetic_example(self):
        self.assertAlmostEqual(crash_rate_per_million_vmt(12, 4_000_000), 3.0)

    def test_zero_crashes(self):
        self.assertEqual(crash_rate_per_million_vmt(0, 100_000), 0.0)

    def test_invalid_crash_counts(self):
        for crashes in (-1, 1.5, True):
            with self.subTest(crashes=crashes), self.assertRaises(ValueError):
                crash_rate_per_million_vmt(crashes, 100_000)

    def test_invalid_exposure(self):
        for vmt in (0, -1, float("inf"), float("nan")):
            with self.subTest(vmt=vmt), self.assertRaises(ValueError):
                crash_rate_per_million_vmt(1, vmt)


if __name__ == "__main__":
    unittest.main()
