def test_get_restaurant_addresses():
    restaurants = [
        {
            "address": "1299 Dough Ave N"
        },
        {
            "address": "6501 Island St SE"
        },
        {
            "address": "12543 Sushi Way NE"
        }
    ]
    addresses = get_restaurant_addresses(restaurants)

    assert addresses == ["1299 Dough Ave N", "6501 Island St SE", "12543 Sushi Way NE"]


def test_get_restaurant_addresses_no_restaurants():
    no_addresses = get_restaurant_addresses([])

    assert no_addresses == []


def get_restaurant_addresses(restaurants):
    addresses = []
    for restaurant in restaurants:
        addresses.append(restaurant["address"])
    return addresses

restaurants = [
        {
            "address": "1299 Dough Ave N"
        },
        {
            "address": "6501 Island St SE"
        },
        {
            "address": "12543 Sushi Way NE"
        }
    ]

# print(get_restaurant_addresses(restaurants))

def get_school_names(schools):
    school_names =[]
    for school in schools:
        school_names.append(schools[school]["name"])
        # print(school)
    return school_names

schools = {
        "school 1": {
            "name": "Western Barkington University",
            "city": "Barkingham"
        },
        "school 2": {
            "name": "University of Barkington",
            "city": "Beattle"
        },
        "school 3": {
            "name": "Barkington State University",
            "city": "Pullbark"
        }
    }

print(get_school_names(schools))
