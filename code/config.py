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

DATA_DISPLAY = dict(
    noneValues={None},
    sectionSep1=" ",
    sectionSep2=":",
    writing="grc",
    writingDir="ltr",
    fontName="Gentium",
    font="GentiumPlus-R.ttf",
    fontw="GentiumPlus-R.woff",
    textFormats={},
    browseNavLevel=2,
    browseContentPretty=False,
)

TYPE_DISPLAY = dict(
    book=dict(
        template="{book}",
        featuresBare="author",
        children="chapter",
        level=3,
        flow="col",
        wrap=False,
        stretch=False,
    ),
    chapter=dict(
        template="{chapter}",
        children="_sentence",
        level=3,
        flow="col",
        wrap=False,
        strectch=False,
    ),
    _sentence=dict(
        template="{_sentence}",
        children="word",
        condense=True,
        level=2,
        flow="row",
        wrap=True,
        strectch=True,
    ),
    _book=dict(
        template="{_book}",
        children="book",
        level=3,
        flow="col",
        wrap=False,
        stretch=False,
    ),
    p=dict(
        template="{p}",
        children="_sentence",
        level=1,
        flow="col",
        wrap=False,
        strectch=False,
    ),
    word=dict(
        template=True,
        base=True,
        level=0,
        flow="col",
        wrap=False,
        strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
