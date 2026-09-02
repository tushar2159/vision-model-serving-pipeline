def validate_response(response: dict) -> bool:
    return isinstance(response, dict) and "task" in response and "result" in response
