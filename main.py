from typing import Dict, List, Optional, Union


def say_hello_world() -> None:
    """
    Print a hello world greeting to the console.
    """
    print("Hello, World!")


def say_hello_to(name: str) -> None:
    """
    Print a personalized greeting to the console.

    Args:
        name (str): The name of the person to greet
    """
    print(f"Hello, {name}!")


def say_goodbye() -> None:
    """
    Print a goodbye message to the console.
    """
    print("Goodbye, World!")


def process_user_data(
    user_id: int, name: str, tags: List[str], metadata: Optional[Dict[str, Union[str, int, bool]]] = None
) -> Dict[str, Union[int, str, List[str]]]:
    """
    Process user data and return formatted information.

    Args:
        user_id (int): The unique identifier for the user
        name (str): The user's name
        tags (List[str]): List of tags associated with the user
        metadata (Optional[Dict[str, Union[str, int, bool]]]): Additional user metadata

    Returns:
        Dict[str, Union[int, str, List[str]]]: Processed user data
    """
    result = {"id": user_id, "name": name, "greeting": f"Hello, {name}!", "tags": tags}

    if metadata:
        result["has_metadata"] = True

    return result


def main() -> None:
    """
    Main function that executes the program workflow.
    Calls the greeting and goodbye functions in sequence.
    """
    say_hello_world()
    say_hello_to("John")

    # Example of using the new function with type hints
    user_data = process_user_data(
        user_id=42, name="Alice", tags=["developer", "python"], metadata={"active": True, "level": 3}
    )
    print(f"Processed user: {user_data['name']}")

    say_goodbye()


if __name__ == "__main__":
    main()
