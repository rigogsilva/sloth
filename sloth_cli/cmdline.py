import json
import typing

from sloth_cli import config
from sloth_cli import parsing
from sloth_cli import profiler


def show_version(**kwargs):
    """Displays the current version"""
    path = config.get_path('settings.json')
    with open(path) as f:
        data = json.load(f)

    print('sloth-cli Version {}'.format(data['version']))
    return data['version']


def show_help():
    """Displays the command help and exits"""
    parsing.parse(['--help'])


def run(arguments: typing.List[str] = None):
    """
    Executes a sloth_cli-cli command action

    :param arguments:
        The command line arguments to parse as a list. If omitted the standard
        sys.argv arguments will be used instead.
    """

    args = parsing.parse(arguments)
    default_action = 'version' if args.pop('version') else None
    action = args.pop('action') or default_action

    actions = dict(
        version=show_version,
        speed=profiler.run
    )
    command = actions.get(action) or show_help
    command(**args)
