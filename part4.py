from part2_producer import connect_to_server
from part2_producer import send_message
from part3 import analyze_sentence
from part3 import get_nlp_pipeline
import json
import sys


if __name__ == '__main__':
    redis_cli, redis_stream_name = connect_to_server()
    pipeline = get_nlp_pipeline()
    while True:
        message = input('Your message (enter "analyze" for sentence analysis): ')
        try:
            message_processed = message.strip().lower()
            if message_processed == 'analyze':
                sentence = input('Your sentence: ')
                json_dict = analyze_sentence(pipeline, sentence)
                message = json.dumps(json_dict, sort_keys=True, indent=4)
            send_message(redis_cli, redis_stream_name, message)
        except Exception as e:
            redis_cli.close()
            print('Error: {0}'.format(str(e)))
            sys.exit('The connection has been interrupted.')
