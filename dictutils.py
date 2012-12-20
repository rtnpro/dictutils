import unittest


def diffdict(s, t):
    """Diffs two dictionaries over both their keys and values.

    This returns a tuple of dicts where each dict is a subset of `s` and `t`
    such that it satisfies the following relationships:

        `added`:   key exists in t but not s

        `removed`: key exists in s but not t

        `updated`: key exists in both s and t but differs in value

        `same`:    key exists in both s and t and has same value
    """
    set_s = set(s)
    set_t = set(t)

    added = dict([(x, t[x]) for x in set_t - set_s])
    removed = dict([(x, s[x]) for x in set_s - set_t])

    same = {}
    updated = {}
    for key in set_s & set_t:
        if s[key] == t[key]:
            same[key] = s[key]
        else:
            updated[key] = t[key]

    return added, removed, updated, same


class DiffDictTests(unittest.TestCase):
    def test_added(self):
        s = dict()
        t = dict(foo=1)
        added, removed, updated, same = diffdict(s, t)
        self.assertDictEqual(dict(foo=1), added)
        self.assertDictEqual(dict(), removed)
        self.assertDictEqual(dict(), updated)
        self.assertDictEqual(dict(), same)

    def test_removed(self):
        s = dict(foo=1)
        t = dict()
        added, removed, updated, same = diffdict(s, t)
        self.assertDictEqual(dict(), added)
        self.assertDictEqual(dict(foo=1), removed)
        self.assertDictEqual(dict(), updated)
        self.assertDictEqual(dict(), same)

    def test_updated(self):
        s = dict(foo=1)
        t = dict(foo=2)
        added, removed, updated, same = diffdict(s, t)
        self.assertDictEqual(dict(), added)
        self.assertDictEqual(dict(), removed)
        self.assertDictEqual(dict(foo=2), updated)
        self.assertDictEqual(dict(), same)

    def test_same(self):
        s = dict(foo=1)
        t = dict(foo=1)
        added, removed, updated, same = diffdict(s, t)
        self.assertDictEqual(dict(), added)
        self.assertDictEqual(dict(), removed)
        self.assertDictEqual(dict(), updated)
        self.assertDictEqual(dict(foo=1), same)


if __name__ == '__main__':
    unittest.main()
