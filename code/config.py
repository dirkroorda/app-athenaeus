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

BASE_TYPE = "word"
CONDENSE_TYPE = "_sentence"

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lemma"}

EXAMPLE_SECTION = "<code>Deipnosophistae 1:1</code>"
EXAMPLE_SECTION_TEXT = "Deipnosophistae 1:1"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = ""
WRITING_DIR = "ltr"

FONT_NAME = "Gentium"
FONT = "GentiumPlus-R.ttf"
FONTW = "GentiumPlus-R.woff"

TEXT_FORMATS = {
    "layout-orig-full": "layoutRich",
}
TEXT_FORMATS = {}


BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False

VERSES = None

LEX = None

TRANSFORM = None

CHILD_TYPE = dict(
    _book="book", book="chapter", chapter="_sentence", p="_sentence", _sentence="word"
)

SUPER_TYPE = None

PLAIN_TYPES = None

PRETTY_TYPES = dict(
    book=("{_book}", "author", ""),
    chapter=("{chapter}", "", ""),
    _sentence=("{_sentence}", "", ""),
    _book=("{_book}", "", ""),
    p=("{p}", "", ""),
    word=(True, "", ""),
)

LEVELS = dict(
    book=dict(level=3, flow="col", wrap=False, stretch=False),
    chapter=dict(level=3, flow="col", wrap=False, strectch=False),
    _sentence=dict(level=2, flow="row", wrap=True, strectch=True),
    _book=dict(level=3, flow="col", wrap=False, stretch=False),
    p=dict(level=1, flow="col", wrap=False, strectch=False),
    word=dict(level=0, flow="col", wrap=False, strectch=False),
)

INTERFACE_DEFAULTS = dict(
    withTypes=True,
    withNodes=False,
    showFeatures=True,
    lineNumbers=None,
    graphics=None,
)


def deliver():
    return (globals(), dirname(abspath(__file__)))
