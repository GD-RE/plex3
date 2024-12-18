"""
Python Lexical Analyser
=======================

The Plex module provides lexical analysers with similar capabilities
to GNU Flex. The following classes and functions are exported;
see the attached docstrings for more information.

   Scanner          For scanning a character stream under the
                    direction of a Lexicon.

   Lexicon          For constructing a lexical definition
                    to be used by a Scanner.

   Str, Any, AnyBut, AnyChar, Seq, Alt, Opt, Rep, Rep1,
   Bol, Eol, Eof, Empty

                    Regular expression constructors, for building pattern
                    definitions for a Lexicon.

   State            For defining scanner states when creating a
                    Lexicon.

   TEXT, IGNORE, Begin

                    Actions for associating with patterns when
                    creating a Lexicon.
"""

#  https://code.google.com/archive/p/python-plex
#  packages.python.org/plex/

__version__ = '2.0.0-fork'
__authors__ = ["Calloc", "GD::RE"]
__former_authors__ = ["Google", "Cython"]

from plex3.actions import TEXT, IGNORE, Begin, Method
from plex3.lexicons import Lexicon, State
from plex3.regexps import RE, Seq, Alt, Rep1, Empty, Str, Any, AnyBut, AnyChar, Range
from plex3.regexps import Opt, Rep, Bol, Eol, Eof, Case, NoCase
from plex3.scanners import Scanner
