
from nicknames.parser import NameDenormalizer

nd = NameDenormalizer()


def nicknames_for(name):
    return nd.get(name,set())
