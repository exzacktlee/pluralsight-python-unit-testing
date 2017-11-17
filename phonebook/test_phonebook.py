import unittest

import phonebook

class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook=phonebook.Phonebook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual('12345', self.phonebook.lookup('Bob'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_not_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_not_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Sue', '123')
        self.assertFalse(self.phonebook.is_consistent())


