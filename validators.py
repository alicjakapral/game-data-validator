ALLOWED_RARITIES = ["Common", "Rare", "Epic", "Legendary"]
REQUIRED_FIELDS = ["id", "name", "price", "rarity"]


def validate_required_fields(item):
    missing_fields = []

    for field in REQUIRED_FIELDS:
        if field not in item:
            missing_fields.append(field)

    if missing_fields:
        missing = ", ".join(missing_fields)
        return f"Missing required fields: {missing}."

    return None


def validate_field_types(item):
    type_errors = []

    if not isinstance(item["id"], int):
        type_errors.append("id must be an integer")

    if not isinstance(item["name"], str):
        type_errors.append("name must be a string")

    if not isinstance(item["price"], (int, float)):
        type_errors.append("price must be a number")

    if not isinstance(item["rarity"], str):
        type_errors.append("rarity must be a string")

    if type_errors:
        return "; ".join(type_errors) + "."

    return None


def validate_name(item):
    if item["name"].strip() == "":
        return f"Item ID {item['id']}: name cannot be empty."

    return None


def validate_price(item):
    if item["price"] < 0:
        return f"Item ID {item['id']}: price cannot be negative ({item['price']})."

    return None


def validate_rarity(item):
    if item["rarity"].strip() == "":
        return f"Item ID {item['id']}: rarity cannot be empty."

    if item["rarity"] not in ALLOWED_RARITIES:
        return f"Item ID {item['id']}: invalid rarity '{item['rarity']}'."

    return None


def validate_id_value(item):
    if item["id"] <= 0:
        return f"Item ID {item['id']}: ID must be greater than 0."

    return None


def validate_duplicate_id(item, used_ids):
    if item["id"] in used_ids:
        return f"Duplicate item ID detected: {item['id']}."

    used_ids.add(item["id"])
    return None