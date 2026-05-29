def validate_intent(intent):

    errors = []

    if not intent.get("app_name"):
        errors.append("missing_app_name")

    if not intent.get("app_type"):
        errors.append("missing_app_type")

    if not intent.get("features"):
        errors.append("missing_features")

    if not intent.get("roles"):
        errors.append("missing_roles")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }