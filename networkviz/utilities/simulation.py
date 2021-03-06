"""
This module provides queries for simulation information.

IMPORTANT!!!
1. It's recommended to use the first method to retrieve the information, where it returns a json object that can be
transferred directly.


Usage:
1. Query combined information (returns json)
    e.g. query_status()
         :returns: a Json object including all information of simulation control

    example return json:

    {
         "dumpall": "FALSE",
         "warn": "TRUE",
         "show_progress": "FALSE",
         "modelname": "model-6268.glm",
         "verbose": "FALSE",
         "clock": "2016-10-06 18:19:13 PDT",
         "realtime_metric": "+0.942004",
         "server_info": "http://gridlabd.slac.stanford.edu:6268",
         "quiet": "FALSE",
         "suppress_repeat_messages": "FALSE",
         "debug": "FALSE"
    }

    c -- clock
    m -- model name
    r -- realtime metric
    v -- verbose
    d -- debug
    a -- dump all
    q -- quiet
    s -- show progress
    u -- suppress repeat messages
    w -- warn
    i -- server_info

2. Status Change
    e.g.  simulation.verbose_off()
          simulation.verbose_on()
    Supports:
        verbose
        debug
        dumpall
        quiet
        show_progress
        suppress_repeat_message
        warn

3. Query single information (returns string)
    e.g. print simulation.clock()

    Available callings:
         simulation.model_name()
         simulation.realtime_metric()
         simulation.verbose()
         simulation.debug()
         simulation.dump_all()
         simulation.quiet()
         simulation.show_progress()
         simulation.suppress_repeat_messages()
         simulation.warn()
         simulation.server_info()

"""
from networkviz.utilities.connection import *
from vaderviz import settings


def query_status(args=''):
    """
    :arg: the information to retrieve
    :return: a Json object including information

    """
    if args == '':
        args = 'mrvdaqsuwi'
    return_value = {}
    for c in args:
        if c in valid_key:
            return_value[valid_key[c]['alias']] = valid_key[c]['callback']()
    return_value['clock'] = clock()
    return json.dumps(return_value)


def verbose_off():
    return set_global(valid_key['v']['basic'], '0')


def verbose_on():
    return set_global(valid_key['v']['basic'], '1')


def debug_off():
    return set_global(valid_key['d']['basic'], '0')


def debug_on():
    return set_global(valid_key['d']['basic'], '1')


def dumpall_off():
    return set_global(valid_key['a']['basic'], '0')


def dumpall_on():
    return set_global(valid_key['a']['basic'], '1')


def quiet_off():
    return set_global(valid_key['q']['basic'], '0')


def quiet_on():
    return set_global(valid_key['q']['basic'], '1')


def show_progress_off():
    return set_global(valid_key['s']['basic'], '0')


def show_progress_on():
    return set_global(valid_key['s']['basic'], '1')


def suppress_repeat_messages_off():
    return set_global(valid_key['u']['basic'], '0')


def suppress_repeat_messages_on():
    return set_global(valid_key['u']['basic'], '1')


def warn_off():
    return set_global(valid_key['w']['basic'], '0')


def warn_on():
    return set_global(valid_key['w']['basic'], '1')


def clock():
    return get_global('clock')


def model_name():
    return get_global(valid_key['m']['basic'])


def realtime_metric():
    return get_global(valid_key['r']['basic'])


def verbose():
    return get_global(valid_key['v']['basic'])


def debug():
    return get_global(valid_key['d']['basic'])


def dump_all():
    return get_global(valid_key['a']['basic'])


def quiet():
    return get_global(valid_key['q']['basic'])


def show_progress():
    return get_global(valid_key['s']['basic'])


def suppress_repeat_messages():
    return get_global(valid_key['u']['basic'])


def warn():
    return get_global(valid_key['w']['basic'])


def server_info():
    return settings.HOSTNAME + ':' + str(settings.PORT)


valid_key = {
    'm': {
        'alias': 'modelname',                   'basic':        'modelname',
        'callback': model_name
    },
    'r': {
        'alias': 'realtime_metric',             'basic':        'realtime_metric',
        'callback': realtime_metric
    },
    'v': {
        'alias': 'verbose',                     'basic':        'verbose',
        'callback': verbose
    },
    'd': {
        'alias': 'debug',                       'basic':        'debug',
        'callback': debug
    },
    'a': {
        'alias': 'dumpall',                     'basic':        'dumpall',
        'callback': dump_all
    },
    'q': {
        'alias': 'quiet',                       'basic':        'quiet',
        'callback': quiet
    },
    's': {
        'alias': 'show_progress',               'basic':        'show_progress',
        'callback': show_progress
    },
    'u': {
        'alias': 'suppress_repeat_messages',    'basic':        'suppress_repeat_messages',
        'callback': suppress_repeat_messages
    },
    'w': {
        'alias': 'warn',                        'basic':        'warn',
        'callback': warn
    },
    'i': {
        'alias': 'server_info',
        'callback': server_info
    },
}
