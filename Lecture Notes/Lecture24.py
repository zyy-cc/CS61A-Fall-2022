import json


def search(query, ranking=lambda r: -r.starts):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)


def review_both(r, s):
    return fast_overlap(r.reviewers, s.reviewers)
    # return len([x for x in r.reviewers if r in s.reviewers])


class Restaurant:
    all = []

    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=review_both):
        """Return the K most similar restaurants to self,
        using SIMILARITY for comparison.
        sorted by default is ascending order
        """
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: - similarity(r, self))[:k]

    def __repr__(self):
        return '<' + self.name + '>'


def fast_overlap(s, t):
    """Return the overlap between sorted S and sorted T
    >>> fast_overlap([2, 3, 5, 6, 7], [1, 4, 5, 6, 7, 8])
    3
    """
    i, j, count = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count


reviewers_for_resaurant = {}
for line in open('reviews,json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_resaurant:
        reviewers_for_resaurant[biz] = [r['user_id']]
    else:
        reviewers_for_resaurant[biz].append(r['user_id'])

for line in open("restaurants.json"):
    r = json.loads(line)
    reviewers = reviewers_for_resaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], sorted(reviewers))

Restaurant('Thai Delight', 2)
Restaurant('Thai Basil', 3)
Restaurant('Top Dog', 5)

results = search(input().strip())
for r in results:
    print(r, "is similar to", r.similar(3))
