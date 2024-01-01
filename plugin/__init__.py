import gettext

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE


def localeInit():
    gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
    gettext.textdomain("enigma2")
    gettext.bindtextdomain("MediaPlayer2", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/MediaPlayer2/locale"))


def _(txt):
    t = gettext.dgettext("MediaPlayer2", txt)
    if t == txt:
        t = gettext.gettext(txt)
    return t


localeInit()
language.addCallback(localeInit)
