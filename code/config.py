from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="pthu",
    repo="athenaeus",
    relative="Athenaeus/Deipnosophistae/tf",
    version="1.1",
    corpus="The Deipnosophistae by Athenaeus",
)

DOCS = dict()

DATA_DISPLAY = dict(writing="grc")

TYPE_DISPLAY = dict(
    book=dict(featuresBare="author"),
    _book=dict(children="book"),
    p=dict(template="{p}", children="_sentence"),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
