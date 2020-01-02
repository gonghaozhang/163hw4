"""
Name: Anastasia Stevens
NetID: asteves
Section: CSE 163 AC
search_engine.py defines a class to manage a collection of documents and handle
computing the relevance of a Document to a given term. It does so by computing
the TF-IDF of a given term for each document that contains the term.
count the words in each document in a directory.
"""

import os
import re
import math
from document import Document


class SearchEngine:
    """
    The SearchEngine class computes the relevance of documents for a given
    term by computing the total TF-IDF of the given term(s) for each document
    that contains the term. The TF-IDF is defined as the product of the term
    frequency of that term and inverse document frequency.

    """
    def __init__(self, dir):
        """
        Constructs a new SearchEngine object given a directory name.

        """
        self._docs = dict()
        self._dir = dir
        self._num_docs = 0
        for file in os.listdir(dir):
            self._num_docs += 1
            doc = Document(dir + '/' + file)
            for word in doc.get_words():
                if word not in self._docs:
                    self._docs[word] = []
                self._docs[word].append(dir + '/' + file)

    def _calculate_idf(self, term):
        """
        Accepts a term, returning the IDF of the term if it exists in this
        SearchEngine, or 0 otherwise. The IDF, or inverse document frequency,
        is defined as the natural log of the total number of documents in this
        Search Engine divided by the number of words in the search engine
        that contain the term. Checks for term occurrence case insensitively
        and ignoring punctuation.
        """
        term = self._ignore_case(term)
        if term not in self._docs:
            return 0
        else:
            num_occ = len(self._docs[term])
            return math.log(self._num_docs/num_occ)

    def search(self, term):
        """
        Accepts one or more terms  and returns a list of document names that
        contain at least one of the terms in descending order of TF-IDF. If no
        document in this SearchEngine contains any of the terms, returns None.
        Searches for terms case-insensitively and ignoring punctuation.
        """
        terms = term.split()
        search = dict()
        for term in terms:
            term = self._ignore_case(term)
            if term in self._docs:
                for file in self._docs[term]:
                    doc = Document(file)
                    term_freq = doc.term_frequency(term)
                    tf_idf = term_freq * self._calculate_idf(term)
                    if file in search:
                        search[file] = search[file] + tf_idf
                    else:
                        search[file] = tf_idf
        sorted_search = sorted(search.items(), key=lambda x: x[1],
                               reverse=True)
        ranked_files = [lis[0] for lis in sorted_search]
        if len(ranked_files) == 0:
            return None
        else:
            return ranked_files

    def _ignore_case(self, term):
        """
        Accepts a term and returns the term lowercase, without any adjacent
        symbols.
        """
        term = term.lower()
        return re.sub(r'\W+', '', term)
