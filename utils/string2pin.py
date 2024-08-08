def get_gpio_pin(pin_name: str):
    try:
        pin = getattr(__import__("board"), pin_name)
        return pin
    except AttributeError:
        raise ValueError(f"Invalid GPIO pin name: {pin_name}")
