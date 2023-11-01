import requests
import asyncio
import json


async def get_mock_response(endpoint_url):
    response_object = requests.get(url=endpoint_url)
    return response_object.json()


async def handle_request(endpoint_url):
    try:
        response_json = await get_mock_response(endpoint_url)
        return {endpoint_url: response_json}
    except requests.exceptions.ConnectTimeout as e:
        print('Time out error: {0}'.format(str(e)))
    except requests.exceptions.RequestException as e:
        print('Request error: {0}'.format(str(e)))
    except Exception as e:
        print('An unknown exception while requesting {0}: {1}'.format(endpoint, str(e)))
    return None


async def main():
    first_endpoint = "https://my-json-server.typicode.com/typicode/demo/posts"
    second_endpoint = "https://my-json-server.typicode.com/typicode/demo/comments"
    third_endpoint = "https://my-json-server.typicode.com/typicode/demo/profile"

    async def aggregate_results():
        results = await asyncio.gather(
            handle_request(first_endpoint),
            handle_request(second_endpoint),
            handle_request(third_endpoint)
        )
        result_dict = {}
        for result in results:
            if result is None:
                continue
            result_dict.update(result)
        return result_dict

    dict_object = await aggregate_results()
    print('See the resulting json below:')
    print(json.dumps(dict_object, sort_keys=True, indent=4))


if __name__ == "__main__":
    asyncio.run(main())
