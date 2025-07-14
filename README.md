This is a collection of testcase mp3-files with embedded synchronized lyrics
(aka SYLT tag).  This set was initially built to verify that [Lollypop][3] player
handles such lyrics correctly, hence the repository also contains a script to
test it, but it might be useful for other projects as well.

# Requirements

* mutagen - to generate tests
* lollypop - to test lollypop

# How to use

All the testcases in the repository can be generated from the `countdown.mp3` with:

    python ./generate-tests.py

The lollypop implementation can be tested with:

    PYTHONPATH="</path/to/lollpop>" python lollypop.test.py

To print lyric parsed by lollypop for a specific file run:

    PYTHONPATH="</path/to/lollpop>" python lollypop.test.py </path/to/file.mp3>

To test lollypop manually:

* Open lollypop
* Under the three dots button at the bottom of the (left) side panel; tick lyrics
* Open a test file in the lollypop
* Switch to the lyrics tab on the side panel

# List of testcases

- `countdown` - the original [file][2] from the [Christian Weiske's blog][1].
  The file doesn't include the SYLT tag, but All the tests are generated based
  upon it.

Encoding tests:

- `iso-nodesc`   - just a simple most basic latin1 lyrics id3v2.3
- `iso-desc`     - lyrics track with nonempty description id3v2.3
- `utf16-nodesc` - utf-16-encoded lyrics without description id3v2.3
- `utf16be-desc` - utf-16be-encoded lyrics with description
- `utf8-nodesc`  - utf-8-encoded lyrics without description
- `utf8-desc`    - utf-8-encoded lyrics with description

Various endline configuration tests

- `endline-reverse`  - endlines are located at the end of the lyrics instead of the beginning
- `extra-line-start` - an additional endline is added at the end of the lyrics
- `extra-line-end`   - an additional endline is added at the beginning of the lyrics
- `extra-line-mid`   - an additional endline is added at the middle (as a e.g. a verse separator)
- `karaoke`          - karaoke-style lyrics i.e. each word is time-codded with multiple words per line
- `multiline`        - some lyrics entries have several lines

# See also

* [Christian Weiske's blog][1], where he describes the current state of the
  SYLT support. Many thanks to him for that article.
* SYLT description in [id3v2.3][4] and [id3v2.4][5](in taglib repository) specs

# Copying

The `countdown.mp3` and all its derivatives are licensed under [CC by-SA 4.0][6].
Original recording was [created][8] by: [tim.kahn][7] and modified by Christian Weiske.

All the code in the repository is licensed under [WTFPL][9].

[1]: https://cweiske.de/tagebuch/embedded-lyrics.htm
[2]: https://cweiske.de/tagebuch/demo/embedded-lyrics/countdown.mp3
[3]: https://wiki.gnome.org/Apps/Lollypop
[4]: https://id3.org/id3v2.3.0#Synchronised_lyrics.2Ftext
[5]: https://github.com/taglib/taglib/blob/e831f0929f25bc581d2106d1f2810f5d8100376e/taglib/mpeg/id3v2/id3v2.4.0-frames.txt#L877
[6]: https://creativecommons.org/licenses/by-sa/4.0/
[7]: https://freesound.org/people/tim.kahn/
[8]: https://freesound.org/people/tim.kahn/sounds/82986/
[9]: https://www.wtfpl.net/
