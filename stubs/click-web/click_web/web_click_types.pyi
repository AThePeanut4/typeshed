'Extra click types that could be useful in a web context as they have corresponding HTML form input type.\n\nThe custom web click types need only be imported into the main script, not the app.py that flask runs.\n\nExample usage in your click command:\n\x08\n    from click_web.web_click_types import EMAIL_TYPE\n    @cli.command()\n    @click.option("--the_email", type=EMAIL_TYPE)\n    def email(the_email):\n        click.echo(f"{the_email} is a valid email syntax.")'

import re
from typing import ClassVar

import click

class EmailParamType(click.ParamType):
    EMAIL_REGEX: ClassVar[re.Pattern[str]]
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

class PasswordParamType(click.ParamType):
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

class TextAreaParamType(click.ParamType):
    def convert(self, value: str, param: click.Parameter | None, ctx: click.Context | None) -> str | None: ...

EMAIL_TYPE: EmailParamType
PASSWORD_TYPE: PasswordParamType
TEXTAREA_TYPE: TextAreaParamType
