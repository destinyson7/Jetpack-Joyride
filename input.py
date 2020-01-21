import signal
from data import *
from alarmexception import AlarmException
from getch import _getChUnix as getChar


def alarmhandler(signum, frame):
    ''' input method '''
    raise AlarmException


def user_input(timeout=0.15):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)

    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
