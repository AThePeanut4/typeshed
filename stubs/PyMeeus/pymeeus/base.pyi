from typing import Final, Literal

TOL: Final = 1e-10

def machine_accuracy() -> tuple[float, int]:
    """
    This function computes the accuracy of the computer being used.

    This function returns a tuple containing the number of significant bits in
    the mantissa of a floating number, and the number of significant digits in
    a decimal number.

    :returns: Number of significant bits, and of significant digits
    :rtype: tuple
    """
    ...
def get_ordinal_suffix(ordinal: float) -> Literal["st", "nd", "rd", "th"]:
    """
    Method to get the suffix of a given ordinal number, like 1'st',
    2'nd', 15'th', etc.

    :param ordinal: Ordinal number
    :type ordinal: int

    :returns: Suffix corresponding to input ordinal number
    :rtype: str
    :raises: TypeError if input type is invalid.

    >>> get_ordinal_suffix(40)
    'th'
    >>> get_ordinal_suffix(101)
    'st'
    >>> get_ordinal_suffix(2)
    'nd'
    >>> get_ordinal_suffix(19)
    'th'
    >>> get_ordinal_suffix(23)
    'rd'
    """
    ...
def iint(number: float) -> int:
    """
    This method behaves in the same way as the **INT()** function described
    by Meeus in his book: Greatest integer which is not greater than number.

    :param number: Number or expresion
    :type number: int, float

    :returns: Greatest integer which is not greater than number
    :rtype: int
    :raises: TypeError if input type is invalid.

    >>> iint(19)
    19
    >>> iint(19.95)
    19
    >>> iint(-2.4)
    -3
    """
    ...
def main() -> None: ...
