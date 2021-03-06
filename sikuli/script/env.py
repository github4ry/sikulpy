import platform
import warnings

from .location import Location
from .robot import Robot
from .sikulpy import unofficial


class Env(object):
    @staticmethod
    def addHotkey(key, modifiers, handler):
        warnings.warn('Env.addHotKey(%r, %r, %r) not implemented' % (key, modifiers, handler))  # FIXME

    @staticmethod
    def removeHotkey(key, modifiers):
        warnings.warn('Env.removeHotKey(%r, %r) not implemented' % (key, modifiers))  # FIXME

    @staticmethod
    def getOS() -> str:
        # FIXME: check that this matches sikuli's OS names
        return platform.system()

    @staticmethod
    def getOSVersion() -> str:
        warnings.warn('Env.getOSVersion() not implemented')  # FIXME

    @staticmethod
    def getSikuliVersion() -> str:
        return "sikulpy 0.0"

    @staticmethod
    def getClipboard() -> str:
        return Robot.getClipboard()

    @staticmethod
    @unofficial
    def putClipboard(text):
        return Robot.putClipboard(text)

    @staticmethod
    def isLockOn(key) -> bool:
        return Robot.isLockOn(key)

    @staticmethod
    def getMouseLocation() -> Location:
        x, y = Robot.getMouseLocation()
        return Location(x, y)
