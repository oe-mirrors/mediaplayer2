from distutils.core import setup
import setup_translate

pkg = 'Extensions.MediaPlayer2'
setup (name = 'enigma2-plugin-extensions-mediaplayer2',
       version = '0.8',
       description = 'MediaPlayer2',
       long_description = 'mediaplayer plugin with added support for subssupport plugin for enhanced subtitles support.',
       author='mx3L and OE-A',
       url='https://github.com/oe-mirrors/mediaplayer2.git',
       package_dir = {pkg: 'plugin'},
       packages = [pkg],
       package_data = {pkg:
           ['MediaPlayer.png', 'keymap.xml', 'locale/*/LC_MESSAGES/*.mo', 'locale/*/LC_MESSAGES/*.po']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
