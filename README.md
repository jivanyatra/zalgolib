# ZalgoLib.py - A Full Zalgo Experience

### "Full"

While Zalgo text's popularity has waned, I'm still a fan. I also have a need for it. Other Zalgo libraries aren't recent, are a part of a larger set of tools, haven't been audited for security recently, or don't offer a lot of customization options.

The goal of this library is to give a decent set of defaults for en-Zalgo-fy [encoding to Zalgo] and de-Zalgo-fy [decoding from Zalgo] text to various degrees, as well as creating a custom class to dial in specific options.

I want to focus on functionality and periodically check in and update as needed. 

### Documentation

#### purpose

I created this as a basic text processing library. It's perfect for running as a default service for an API, cloud FaaS, CLI core process, etc. It acts as drop-in functionality for learning new frameworks. It's also useful in a series of horror short stories I wrote that was presented as a hosted API at one point in time. You had to make API calls to get chunks of the story, which gradually become more and more corrupt, and then you unlocked access to the `dezalgofy` function to be able to read later sections, including the real ending.

##### dependencies

`random` (standard library) is the only dependency required. I've writing this library in **python 3.7**, but I expect it should work fairly well with a wider set of python versions. The key is my use of `random.choices()` - if this isn't importable, you'll need to adjust and tweak. I use it to select from the lists of diacritics _with replacement_. 

#### installation

`pip install zalgolib` should be sufficient to install, as this package has been [released on PyPI](https://pypi.org/project/zalgolib/). As usual, use a virtual environment if at all possible. I should probably come up with a CLI app that is installable on Linux, and maybe have it as an API service in a docker container...

##### zalgolib.py

* `enzalgofy` : takes two keyword arguments (`text` and `intensity`).
  * `text` expects a `string` as input - you can feed it from whatever source you want.
  * `intensity` expects an `int` from `0-100` (inclusive) and represents a rough percentage of the marks to include on each character. **The default is 50.** This scales up quite quickly, with values less than 20 being fairly light and values over 75 being very heavy. The differences lower or higher (respectively) from those points have some diminishing returns on legibility.
    * In the future, I'd like to adjust this to provide some more variability from character to character within a block of text. I'd like to make this available as a parameter as well.

* `dezalgofy` : takes a zalgo `string`, converts it to ascii, and then back to utf-8. It ignores all errors. This isn't great overall, since if you're adding text that's accented already, it will return a stripped version of it. To be fair, that problem seems sufficiently complex to solve, and probably benefits from a language specifier and dictionaries, or some ML magic. As it is, it's fairly lean and does the job.

##### diacritics.py

This contains the various diacritics used in creating zalgo text. Currently, it contains:

* "DOWN_MARKS": marks that appear below a given character as `list`. There are currently 40 of these.
* "DOWN_LEN": length of `DOWN_MARKS` as `int`
* "UP_MARKS": marks that appear above a given character as `list`. There are currently 46 of these.
* "UP_LEN": length of `UP_MARKS` as `int`
* "MID_MARKS": marks that appear in the middle of, directly over, or overlapping the character slightly in front of or behind as `list`. There are currently 21 of these.
* "MID_LEN": length of `MID_MARKS` as `int`

This is a work-in-progress. There are many more overlapping marks to be found in the unicode space. I hope to revisit these soon and include some of the ones specified below:

* [Extended Combining Diacritical Marks](https://unicode-table.com/en/blocks/combining-diacritical-marks-extended/)
* [Combining Diacritical Marks](https://en.wikipedia.org/wiki/Combining_Diacritical_Marks)
* Markers from other languages such as Arabic, Hebrew, Hindi, Bengali, Oriya, Malayalam, Tamil, etc.

These python lists can be added to in your script, but you'll have to recalculate the lengths (since length calculation from the module is done at import). Conversely, you can just append the characters to `diacritics.py` as you see fit, either by adding them to the list or adding them as new lists.

### To-Do

* add additional readily-available diacritics
* add variability to number of diacritics added per character
  * based on text input
  * make parameter available for adjusting
  * perhaps add option for random variability?
* ~~add scaffolding to publish to PyPI~~
* ~~publish to PyPI~~

### License

I went with a permissive license (MIT) so feel free to use this any way you want. If you're proud of what you've made with my library, feel free to reach out and I'll try to add your project to a list below. Also, please check the credits section below, which also contributed to my choice to go with the MIT license.

### Credit

I am utilizing the list of diacritics that was carefully and conveniently laid out by [Gregory Neal](https://github.com/gregoryneal/) in his [Zalgo implementation](https://github.com/gregoryneal/zalgo/blob/master/code/zalgo_text/zalgo.py). Huge thanks to him for not only being a great programmer, but also using a very permissive MIT license that allows me to use a part of his work for my own. Just because I don't have to credit him doesn't mean I won't.
