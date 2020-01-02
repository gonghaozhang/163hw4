from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


def test_document_class_1():
    file = 'cutedog.txt'
    test = Document(file)

    # Tests example given in prompt
    assert_equals(.5, test.term_frequency('cutest'))
    assert_equals(.25, test.term_frequency('the'))
    assert_equals(.25, test.term_frequency('dog'))
    assert_equals(0, test.term_frequency('cat'))
    assert_equals(['the', 'cutest', 'dog'], test.get_words())


def test_document_class_2():
    file = 'empty.txt'
    test = Document(file)

    # Tests Document object representing empty file
    assert_equals([], test.get_words())
    assert_equals(0, test.term_frequency('dogs'))
    assert_equals(file, test._file_name)
    assert_equals({}, test._term_frequency)


def test_document_class_3():
    file = 'casesensitive.txt'
    test = Document(file)

    # Tests case insensitivity and puncutation ignoring
    assert_equals({'hello': 1.0}, (test._term_frequency))
    assert_equals(0, test.term_frequency('DOG'))
    assert_equals(1, test.term_frequency('hello'))
    assert_equals(1, test.term_frequency('HELLO!'))


def test_search_engine_1():
    test = SearchEngine('test_dir1')

    # Tests small number of words
    assert_equals('test_dir1', test._dir)
    assert_equals(5, test._num_docs)
    assert_equals(0, test._calculate_idf('Cat'))
    assert_equals(.223, test._calculate_idf('I'))
    assert_equals(1.609, test._calculate_idf('dogs'))
    assert_equals(['doc3.txt'], test.search('dogs'))
    assert_equals(['doc3.txt'], test.search('dogs'))
    assert_equals(['doc4.txt', 'doc1.txt'], test.search('eat'))
    assert_equals(['doc4.txt', 'doc3.txt', 'doc1.txt'],
                  test.search('eat dogs'))


def test_search_engine_2():
    test = SearchEngine('test_dir2')

    # Tests large number of words
    assert_equals(4, test._num_docs)
    assert_equals(.287, test._calculate_idf('Samsung'))
    assert_equals(['ChromeBook.html', 'att.html', 'facebook.html'],
                  test.search('Samsung'))
    assert_equals(['ChromeBook.html', 'att.html', 'facebook.html'],
                  test.search('Samsung companies!'))
    assert_equals(None, test.search('adksamfk'))


def test_search_engine_3():
    test = SearchEngine('test_dir3')

    # Tests Empty Directory
    assert_equals(1, test._num_docs)
    assert_equals({}, test._docs)
    assert_equals(0, test._calculate_idf('Samsung'))
    assert_equals(None, test.search('Samsung'))


def main():
    test = SearchEngine('test')
    print(test.search('corgis'))
    print(test.search('love corgis'))

    """
    test_document_class_1()
    test_document_class_2()
    test_document_class_3()
    test_search_engine_1()
    test_search_engine_2()
    test_search_engine_3()
    """


if __name__ == "__main__":
    main()
