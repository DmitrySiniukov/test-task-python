import redis
import os
import sys


def send_message(redis_cli, stream_name, message):
    try:
        redis_cli.xadd(stream_name, {'message': message})
    except ConnectionError as e:
        print("ERROR: REDIS CONNECTION: {0} ".format(e))
        raise e
    except Exception as e:
        print("ERROR: REDIS: {0} ".format(e))
        raise e


def connect_to_server():
    redis_port = os.environ.get('REDIS_PORT', '6005')
    try:
        redis_port_int = int(redis_port)
    except ValueError:
        redis_port_int = 6005
    redis_cli = redis.Redis(host='127.0.0.1', port=redis_port_int)

    redis_steam_name = os.environ.get('STREAM_NAME', 'messages_stream')

    return redis_cli, redis_steam_name


if __name__ == "__main__":
    redis_cli, redis_stream_name = connect_to_server()
    while True:
        message = input('Your message: ')
        try:
            send_message(redis_cli, redis_stream_name, message)
        except Exception as e:
            redis_cli.close()
            print('Error: {0}'.format(str(e)))
            sys.exit('The connection has been interrupted.')
