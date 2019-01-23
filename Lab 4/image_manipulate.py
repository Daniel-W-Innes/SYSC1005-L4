from Cimpl import *
import random


def red_channel(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> red_channel(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(r, 0, 0))


def green_channel(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> green_channel(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(0, g, 0))


def blue_channel(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> blue_channel(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(0, 0, b))


def reduce_brightness(image, percentage):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> reduce_brightness(image, percentage)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(r * percentage, g * percentage, b * percentage))


def swap_red_blue(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> swap_red_blue(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(b, g, r))


def hide_image(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> hide_image(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color((r + g + b)/3/10, random.randint(0, 255), random.randint(0, 255)))


def recover_image(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> hide_image(image)
    >>> show(image)
    >>> recover_image(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(r * 10, r * 10, r * 10))


def test_red_channel():
    image = load_image(choose_file())
    show(image)
    red_channel(image)
    show(image)


def test_green_channel():
    image = load_image(choose_file())
    show(image)
    green_channel(image)
    show(image)


def test_blue_channel():
    image = load_image(choose_file())
    show(image)
    blue_channel(image)
    show(image)


def test_reduce_brightness():
    image = load_image(choose_file())
    percentage = input("percentage")
    show(image)
    reduce_brightness(image, percentage)
    show(image)


def test_swap_red_blue():
    image = load_image(choose_file())
    show(image)
    swap_red_blue(image)
    show(image)


def test_hide_image():
    image = load_image(choose_file())
    show(image)
    hide_image(image)
    show(image)
    save_as(image, choose_save_filename("hided_image"))


def test_recover_image():
    image = load_image(choose_file())
    show(image)
    recover_image(image)
    show(image)
