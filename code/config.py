from os.path import dirname, abspath

PROTOCOL = 'http://'
HOST = 'localhost'
PORT = dict(
    kernel=19610,
    web=9610,
)

OPTIONS = ()

ORG = 'pthu'
REPO = 'patristics'
CORPUS = 'The Deipnosophistae by Athenaeus'
VERSION = '1.0'
RELATIVE = 'Athenaeus/Deipnosophistae/tf'

DOI_TEXT = '10.5281/zenodo.nnn'
DOI_URL = 'https://doi.org/10.5281/zenodo.nnn'

DOC_URL = (
    'https://nbviewer.jupyter.org/github/pthu/patristics'
    '/blob/master/docs/transcription.md'
)
DOC_INTRO = ''
CHAR_URL = DOC_URL
CHAR_TEXT = 'How TF features represent text'

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

CONDENSE_TYPE = 'chapter'

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {'lemma'}

EXAMPLE_SECTION = '<code>Deipnosophistae 1:1</code>'
EXAMPLE_SECTION_TEXT = 'Deipnosophistae 1:1'

SECTION_SEP1 = ' '
SECTION_SEP2 = ':'

DEFAULT_CLS = 'txtn'
DEFAULT_CLS_ORIG = 'txtp'

FORMAT_CSS = dict(
    full='txtp',
    plain='txtp',
)

CLASS_NAMES = None

FONT_NAME = 'Gentium'
FONT = 'GentiumPlus-R.ttf'
FONTW = 'GentiumPlus-R.woff'

TEXT_FORMATS = {
    'layout-orig-full': 'layoutRich',
}
TEXT_FORMATS = {}


BROWSE_NAV_LEVEL = 3
BROWSE_CONTENT_PRETTY = False


def deliver():
  return (globals(), dirname(abspath(__file__)))
