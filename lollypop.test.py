#!/usr/bin/env python
# To run all tests:
#        PYTHONPATH="/path/to/lollpop" python lollypop.test.py
# to dump lyrics for a specific file:
#        PYTHONPATH="/path/to/lollpop" python lollypop.test.py </path/to.mp3>
import pathlib
import sys

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstPbutils', '1.0')
gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')

from gi.repository import Gst
Gst.init(None)

from lollypop.tagreader import TagReader, Discoverer

import unittest

def test_uri(fn):
    return uri(pathlib.Path(__file__).parent / "tests" / fn)

def uri(fn):
    return "file://" + str(pathlib.Path(fn).resolve())

def get_lyrics(uri):
    tagreader = TagReader()
    discoverer = Discoverer()
    info = discoverer.get_info(uri)

    return tagreader.get_synced_lyrics(info.get_tags())

class TestSequense(unittest.TestCase):
    pass

def generate_parametric_tests():
    def test_generator(t, data):
        def do_test(self):
            self.assertEqual(get_lyrics(test_uri(t + ".mp3")), data)
        return do_test

    tests = [ ( ["iso-desc", "iso-nodesc", "extra-line-start", "extra-line-end", "endline-reverse", "noendline"],
                [('ten', 0), ('nine', 1000), ('eight', 2000), ('seven', 3000), ('six', 4000),
                 ('5', 5000), ('4', 6000), ('3', 7000), ('2', 8000), ('1', 9000), ('0', 10000)
                 ]),
              ( ["utf16be-desc", "utf16-nodesc", "utf8-desc", "utf8-nodesc"],
                [('десять', 0), ('девять', 1000), ('восемь', 2000), ('семь', 3000), ('шесть', 4000),
                 ('5', 5000), ('4', 6000), ('3', 7000), ('2', 8000), ('1', 9000), ('0', 10000)
                 ]),
              ( [ "extra-line-mid" ],
                [('ten', 0), ('nine', 1000), ('eight', 2000), ('seven', 3000), ('six', 4000), ("", 5000),
                 ('5', 5000), ('4', 6000), ('3', 7000), ('2', 8000), ('1', 9000), ('0', 10000)
                 ]),
              ( ["multiline"],
                [('ten', 0),
                 ('nine', 0),
                 ('eight', 2000),
                 ('    seven', 2000),
                 ('        six', 2000),
                 ('5', 5000),
                 ('4', 5000),
                 ('3', 7000),
                 ('  2', 7000),
                 ('    1', 7000)
                 ]),
               ( [ "karaoke" ],
                 [('ten nine eight seven six', 0),
                  ('5 4 3 2 1', 5000),
                  ('0', 10000)
                  ]),
               ( [ "countdown" ], [] )
             ]
    for (t_list, t_data) in tests:
        for t in t_list:
            test_name = 'test_%s' % t
            test = test_generator(t, t_data)
            setattr(TestSequense, test_name, test)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for (l,t) in get_lyrics(uri(sys.argv[1])):
            print("[%d]%s\n" % (t,l))
    else:
        generate_parametric_tests()
        unittest.main()
