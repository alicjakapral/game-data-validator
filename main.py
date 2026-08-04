import json

from validators import (
    validate_required_fields,
    validate_field_types,
    validate_name,
    validate_price,
    validate_rarity,
    validate_id_value,
    validate_duplicate_id,
)


DATA_FILE = "items.json"


def load_items(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    items = load_items(DATA_FILE)

    validators = [
        validate_name,
        validate_price,
        validate_rarity,
        validate_id_value,
    ]

    used_ids = set()
    errors = []

    for index, item in enumerate(items, start=1):
        required_fields_error = validate_required_fields(item)

        if required_fields_error:
            errors.append(f"Item #{index}: {required_fields_error}")
            continue

        field_types_error = validate_field_types(item)

        if field_types_error:
            errors.append(f"Item #{index}: {field_types_error}")
            continue

        for validator in validators:
            error = validator(item)

            if error:
                errors.append(error)

        duplicate_id_error = validate_duplicate_id(item, used_ids)

        if duplicate_id_error:
            errors.append(duplicate_id_error)

    print("=" * 40)
    print("GAME DATA VALIDATOR")
    print("=" * 40)
    print(f"File: {DATA_FILE}")
    print(f"Items checked: {len(items)}")
    print(f"Errors found: {len(errors)}")
    print()

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
    else:
        print("[OK] No validation errors found.")

    print()
    print("Validation finished.")


if __name__ == "__main__":
    main()