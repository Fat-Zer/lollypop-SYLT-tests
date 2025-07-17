#!/usr/bin/env python

from mutagen.id3 import ID3, SYLT, TIT2, Encoding

import os, sys
from shutil import copyfile
import pathlib

script_path = pathlib.Path(__file__).parent
source_file = script_path / "tests" / "countdown.mp3"

def create_test(name, data, v2_version=4):
    fn = script_path / "tests" / "{0}.mp3".format(name)
    copyfile (source_file,  fn)

    print("Generating test %s: %s" % (fn.name, data))

    data.setdefault('encoding', Encoding.UTF8)
    data.setdefault('lang', "eng")
    data.setdefault('format', 2)
    data.setdefault('type', 1)

    tag = ID3 (fn)
    tag.add(TIT2(text=name))
    tag.setall("SYLT", [SYLT(**data)])
    tag.save(v2_version=v2_version)

eng_text = [('\nten', 0),
            ('\nnine', 1000),
            ('\neight', 2000),
            ('\nseven', 3000),
            ('\nsix', 4000),
            ('\n5', 5000),
            ('\n4', 6000),
            ('\n3', 7000),
            ('\n2', 8000),
            ('\n1', 9000),
            ('\n0', 10000)]

rus_text = [(u'\nдесять', 0),
            (u'\nдевять', 1000),
            (u'\nвосемь', 2000),
            (u'\nсемь',   3000),
            (u'\nшесть', 4000),
            (u'\n5', 5000),
            (u'\n4', 6000),
            (u'\n3', 7000),
            (u'\n2', 8000),
            (u'\n1', 9000),
            (u'\n0', 10000)]

create_test("iso-nodesc", {'encoding' : Encoding.LATIN1,
                           'text' : eng_text},
            v2_version=3)
create_test("iso-desc", {'encoding' : Encoding.LATIN1,
                         'desc' : 'Some Description String', 
                         'text' : eng_text},
            v2_version=3)
create_test("utf16-nodesc", {'encoding' : Encoding.UTF16,
                             'lang' : 'rus',
                             'text' : rus_text},
            v2_version=3)
create_test("utf16be-desc", {'encoding' : Encoding.UTF16BE,
                             'lang' : 'rus',
                             'desc' : u'Некоторое описание', 
                             'text' : rus_text})
create_test("utf8-desc", {'encoding' : Encoding.UTF8,
                          'lang' : 'rus',
                          'desc' : u'Некоторое описание', 
                          'text' : rus_text})
create_test("utf8-nodesc", {'encoding' : Encoding.UTF8,
                            'lang' : 'rus',
                            'text' : rus_text})

create_test("extra-line-end", { 'text' : eng_text + [('\n', 11000)]})
create_test("extra-line-start", { 'text' :  [('\n', 0)] + eng_text })
create_test("extra-line-mid", { 'text' :  eng_text[:5] + [('\n', 5000)] + eng_text[5:] })
create_test("noendline", { 'text' : [ (l.strip('\n'), t) for (l,t) in eng_text] })
create_test("endline-reverse", { 'text' : [ (l.strip('\n')+'\n', t) for (l,t) in eng_text] })

create_test("multiline", { 'text' :[("\nten" + 
                                     "\nnine", 0),
                                    ("\neight" +
                                     "\n    seven" +
                                     "\n        six", 2000),
                                    ("\n5" +
                                     "\n4", 5000),
                                    ("\n3" +
                                     "\n  2" +
                                     "\n    1", 7000)]})

create_test("karaoke", { 'text' :[
      ('ten', 0), (' nine', 1000), (' eight', 2000), (' seven', 3000), (' six', 4000),
      ('\n5', 5000), (' 4', 6000), (' 3', 7000), (' 2', 8000), (' 1', 9000),
      ('\n0', 10000)
    ]})
