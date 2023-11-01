import os
import redis.asyncio as redis
import asyncio


async def main():
    redis_port = os.environ.get('REDIS_PORT', '6005')
    try:
        redis_port_int = int(redis_port)
    except ValueError:
        redis_port_int = 6005

    redis_steam_name = os.environ.get('STREAM_NAME', 'messages_stream')

    last_id = '$'
    redis_connection = await redis.Redis(host='127.0.0.1', port=redis_port_int)

    while True:
        # Read the stream
        try:
            response = await redis_connection.xread(
                {redis_steam_name: last_id},
                count=1,
                block=1000
            )
            if response:
                key, messages = response[0]
                last_id, payload = messages[0]
                message_json = {key.decode(): value.decode("utf-8") for key, value in payload.items()}
                print('{0}: {1}'.format(last_id.decode(), message_json.get('message', '')))
            else:
                pass
                # todo: implement an exit condition
        except ConnectionError as e:
            print("ERROR: REDIS CONNECTION: {} ".format(e))
        except Exception as e:
            print("ERROR: REDIS: {} ".format(e))
            await redis_connection.close()


if __name__ == "__main__":
    asyncio.run(main())
