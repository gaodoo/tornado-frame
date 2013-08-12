#!/usr/bin/env python
# encoding: utf-8

from os import path
import importlib
import sys
from pkgutil import iter_modules
import optparse

class Commands(object):
    default_settins = {}

    def __init__(self):
        self.settings = None

    def syntax(self):
        return ""

    def short_desc(self):
        return ""

    def long_desc(self):
        return self.short_desc()

    def help(self):
        return self.long_desc()

    def add_options(self, parser):
        group = optparse.OptionGroup(parser, "Global Options")
        group.add_options('--logfile', metavar="FILE",
            help="logfile, user stderr")
        parser.add_option_group(group)

    def process_options(self, args, opts):
        pass

    def run(self, args, opts):
        raise NotImplementedError


def _get_settings():
    project_dir = path.dirname(__file__)
    settings_file = path.join(project_dir, 'settings.py')
    try:
        settings = importlib.import_module('setttings.py')
    except ImportError:
        print "import settings.py fails"
        sys.exit()

def _walk_commands(path="commands"):
    command_mod = importlib.import_module(path)
    mods = []
    if hasattr(command_mod, '__path__'):
        for _, subpath, ispkg in iter_modules(command_mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += _walk_commands(fullpath)
            else:
                submod = importlib.import_module(fullpath)
                mods.append(submod)
    return mods

def execute():
    cmds = _walk_commands()
    cmdname = sys.argv.pop(0)

    parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),
        conflict_handler='resolve')

    # cmd exception handler
    if not cmdname:
        print "not command name given"
        sys.exit(0)
    elif cmdname not in cmds:
        print "unknow commands %s" % cmdname
        sys.exit(0)
    cmd = cmds[cmdname]

    parse.usage = "scrapy %s %s " % (cmdname, cmd.syntax())
    parse.description = cmd.long_desc()
    settings = _get_settings()
    cmd.settings = settings.update(cmd.default_settings)
    cmd.add_options(parser)
    opts, args = parser.parse_args(args=sys.argv)
    _run_print_help(parser, cmd.process_options, args, opts)
    _run_print_help(parser, cmd.run, args, opts)

def _run_print_help(parser, func, *args, **kw):
    try:
        func(*a, **kw)
    except UsageError, e:
        if str(e):
            parser.error(str(e))
        if e.print_help:
            parser.print_help()
        sys.exit(0)

if __name__ == '__main__':
    execute()
