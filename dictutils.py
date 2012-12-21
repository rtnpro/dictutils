import unittest


def diffdicts(s, t):
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
    def assertDiff(self, s, t, added=None, removed=None, updated=None,
                   same=None):
        _added, _removed, _updated, _same = diffdicts(s, t)
        self.assertDictEqual(added or {}, _added)
        self.assertDictEqual(removed or {}, _removed)
        self.assertDictEqual(updated or {}, _updated)
        self.assertDictEqual(same or {}, _same)

    def test_added(self):
        s = dict()
        t = dict(foo=1)
        self.assertDiff(s, t, added=dict(foo=1))

    def test_removed(self):
        s = dict(foo=1)
        t = dict()
        self.assertDiff(s, t, removed=dict(foo=1))

    def test_updated(self):
        s = dict(foo=1)
        t = dict(foo=2)
        self.assertDiff(s, t, updated=dict(foo=2))

    def test_same(self):
        s = dict(foo=1)
        t = dict(foo=1)
        self.assertDiff(s, t, same=dict(foo=1))


if __name__ == '__main__':
    unittest.main()
