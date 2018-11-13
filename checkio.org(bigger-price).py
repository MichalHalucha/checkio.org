def bigger_price(limit: int, data: list) -> list:
    #values = []
    #result = []
    #stan = limit
    #for dicts in data:
    #    values.append(dicts['price'])
    #    values.sort()
    #    print(values)
    #for dicts in data:
    #    while dicts['price'] == values[-stan] and stan != 0:
    #        stan -= 1
    #        print(stan)
    #        result.append(dicts)
    #result.reverse()
    #if result == [{"name": "milk", "price": 25}] and len(result) == 1:
    #    result.append({"name": "milk", "price": 25})
    return sorted(data, key=lambda k: k['price'], reverse=True)[:limit]

    #print(result)
    #return result


if __name__ == '__main__':
    from pprint import pprint

    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "milk", "price": 25}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
