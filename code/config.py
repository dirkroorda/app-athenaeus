from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=19610, web=9610)

ORG = "pthu"
REPO = "athenaeus"
CORPUS = "The Deipnosophistae by Athenaeus"
VERSION = "1.1"
RELATIVE = "Athenaeus/Deipnosophistae/tf"

DOI_TEXT = "10.5281/zenodo.nnn"
DOI_URL = "https://doi.org/10.5281/zenodo.nnn"

DOC_URL = (
    "https://nbviewer.jupyter.org/github/pthu/patristics"
    "/blob/master/docs/transcription.md"
)
DOC_INTRO = ""
CHAR_URL = DOC_URL
CHAR_TEXT = "How TF features represent text"

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

EXAMPLE_SECTION = "<code>Deipnosophistae 1:1</code>"
EXAMPLE_SECTION_TEXT = "Deipnosophistae 1:1"

DATA_DISPLAY = dict(writing="grc",)

TYPE_DISPLAY = dict(
    book=dict(featuresBare="author",),
    _book=dict(children="book",),
    p=dict(template="{p}", children="_sentence",),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
