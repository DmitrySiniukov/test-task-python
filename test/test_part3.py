import unittest
from mock import patch


class TestPart3(unittest.TestCase):

    def test_analyze_sentence(self):
        from part3 import analyze_sentence

        mocked_results = []
        def nlp_pipeline(sentence):
            return mocked_results

        result = analyze_sentence(nlp_pipeline, 'test sentence.')
        self.assertEqual(result, {})

        with patch('part3.abbreviations', {'test_group_label': 'test_group'}):
            mocked_results = [{'word': 'test_word', 'entity_group': 'test_group_label'}]
            result = analyze_sentence(nlp_pipeline, '')
            self.assertEqual(result, {'test_word': 'test_group'})
