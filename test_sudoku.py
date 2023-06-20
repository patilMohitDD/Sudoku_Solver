from main import square_area
from json import loads


db = {}
with open('db.json') as f:
    db = loads(f.read())


def testMatrixLength():
    for values in db.values():
        assert len(values) == 9

def testTypeOfKeys():
    for keys in db.keys():
        assert type(keys) == str


# def testArea():
#     assert square_area(5) == 25
    