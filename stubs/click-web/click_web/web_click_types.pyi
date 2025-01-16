'Extra click types that could be useful in a web context as they have corresponding HTML form input type.\n\nThe custom web click types need only be imported into the main script, not the app.py that flask runs.\n\nExample usage in your click command:\n\x08\n    from click_web.web_click_types import EMAIL_TYPE\n    @cli.command()\n    @click.option("--the_email", type=EMAIL_TYPE)\n    def email(the_email):\n        click.echo(f"{the_email} is a valid email syntax.")'

import re
import typing as t

import click

class EmailParamType(click.ParamType):
    EMAIL_REGEX: re.Pattern[str]
    def convert(self, value: t.Any, param: click.Parameter | None, ctx: click.Context | None) -> t.Any: ...

class PasswordParamType(click.ParamType):
    def convert(self, value: t.Any, param: click.Parameter | None, ctx: click.Context | None) -> t.Any: ...

class TextAreaParamType(click.ParamType):
    def convert(self, value: t.Any, param: click.Parameter | None, ctx: click.Context | None) -> t.Any: ...

EMAIL_TYPE: EmailParamType
PASSWORD_TYPE: PasswordParamType
TEXTAREA_TYPE: TextAreaParamType
