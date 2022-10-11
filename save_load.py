import json
from brand import Brand


def save_data(brands):
    json_brands = []

    for brand in brands:
        save_brand = {"name": brands[brand].name, "price": brands[brand].price,
                      "salePrice": brands[brand].salePrice, "kg": brands[brand].kg,
                      "offer": brands[brand].offer}
        json_brands.append(save_brand)

    with open(f'brandsData/brands_data.json', 'w') as f:
        json.dump(json_brands, f, indent=4)


def load_data(brands):
    with open(f"brandsData/brands_data.json", "r") as x:
        brands_data = json.load(x)
        for brand in brands_data:
            new_brand = Brand(brand["name"], brand["price"], brand["salePrice"], brand["kg"], brand["offer"])
            brands[new_brand.name] = new_brand


def load_brands(brands):
    try:
        load_data(brands)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass