def wildcard_match(pattern, text, case_insensitive: bool = True):
    """
    Performs a case-insensitive wildcard match against two strings.
    This method works with pseduo-regex chars; specifically ? and * are supported.
    An asterisk (*) represents any combination of characters.
    A question mark (?) represents any single character.
    :param str pattern: the regex-like pattern to be compared against
    :param str text: the string to compare against the pattern
    :param boolean case_insensitive: dafault is True
    return whether the text matches the pattern
    """
    ...
