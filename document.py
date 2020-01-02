"""
Name: Anastasia Stevens
NetID: asteves
Section: CSE 163 AC
document.py defines a class to find the term frequency of each unique word in a
document.
"""

import re


class Document:
    """
    The Document class represents a document and contains methods related to
    the term frequency of unique words in this document. Uniqueness is
    case-insensitive and ignores punctuation and non-alphabetic characters.
    (ie. “hello” and “HeLo!?!” are considered the same word.) Term frequency
    is the number of occurrences of a given word divided by the total words in
    the document.
    """

    def __init__(self, file_name):
        """
        Initializes a new Document object. Accepts a file name (file_name)
        which is the name of the file this Document will represent.
        """
        self._term_frequency = self._compute_term_frequency(file_name)
        self._file_name = file_name

    def _compute_term_frequency(self, file_name):
        """
        Returns a dictionary of all of the unique words in the file called
        file_name mapped to their respective term frequencies. Uniqueness is
        case-insensitive and ignores punctuation and non-alphabetic characters.
        (ie. “hello” and “HeLo!?!” are considered the same word.) Term
        frequency is the number of occurrences of a given word divided by the
        total words in the document.
        """
        term_frequency = dict()
        with open(file_name) as f:
            tokens = f.read().split()
            length = len(tokens)
            for token in tokens:
                token = self._ignore_case(token)
                if token in term_frequency:
                    term_frequency[token] = ((term_frequency[token] * length)
                                             + 1)/length
                else:
                    term_frequency[token] = 1/length
        return term_frequency

    def term_frequency(self, term):
        """
        Accepts a term and returns the term frequency of the given term or 0 if
        the term is not present in this Document. Term frequency is defined as
        the number of occurrences of a given word divided by the total words in
        the document.
        """
        term = self._ignore_case(term)
        if term in self._term_frequency:
            return self._term_frequency[term]
        else:
            return 0

    def get_words(self):
        """
        Returns a list of all of the unique words in this Document. Uniqueness
        is case-insensitive and ignores punctuation and non-alphabetic
        characters. (ie. “hello” and “HeLo!?!” are considered the same word.)
        """
        return list(self._term_frequency.keys())

    def _ignore_case(self, term):
        """
        Accepts a term and returns the term lowercase, without any adjacent
        symbols.
        """
        term = term.lower()
        return re.sub(r'\W+', '', term)
