def validate_schema_consistency(schema):

    errors = []

    try:

        api_endpoints = schema["api"]["endpoints"]

        db_tables = schema["database"]["tables"]

        db_fields = set()

        for table in db_tables:

            for column in table["columns"]:

                db_fields.add(
                    column["name"]
                )

        for endpoint in api_endpoints:

            if "request_body" in endpoint:

                for field in endpoint["request_body"]:

                    if field not in db_fields:

                        errors.append(
                            f"api_db_mismatch:{field}"
                        )

    except Exception as e:

        errors.append(
            f"validation_error:{str(e)}"
        )

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }