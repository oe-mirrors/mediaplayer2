import gettext

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

PluginLanguageDomain = 'MediaPlayer2'
PluginLanguagePath = 'Extensions/MediaPlayer2/locale'

def localeInit():
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
    t = gettext.dgettext(PluginLanguageDomain, txt)
    if t == txt:
        print('[%s] fallback to default translation for %s' % (PluginLanguageDomain, txt))
        t = gettext.gettext(txt)
    return t


localeInit()
language.addCallback(localeInit)
