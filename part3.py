from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

abbreviations = {
    'LOC': 'location',
    'ORG': 'organization',
    'PER': 'person',
    'MISC': 'miscellaneous'
}


def get_nlp_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)


def analyze_sentence(nlp_pipeline, sentence):
    ner_results = nlp_pipeline(sentence)
    if not ner_results:
        return {}

    results = {}
    for item in ner_results:
        results[item['word']] = abbreviations.get(item['entity_group'])
    return results


if __name__ == '__main__':
    nlp_pipeline = get_nlp_pipeline()
    while True:
        sentence = input('Your sentence: ')
        results = analyze_sentence(nlp_pipeline, sentence)
        if not results:
            print('Result: no entities.')
        else:
            print('Results:')
            for key, value in results.items():
                print('    {0}: {1}'.format(key, value))
