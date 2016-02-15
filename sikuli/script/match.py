"""
http://doc.sikuli.org/match.html
"""

from .region import Region
from .rectangle import Rectangle
from .location import Location


class Match(Region):
    def __init__(self, rect: Rectangle, sim: float, targetOffset: Location):
        super().__init__(rect)
        self._score = sim
        self._targetOffset = targetOffset

    def getScore(self) -> float:
        """
        Get the similarity score the image or pattern was found. The value
        is between 0 and 1.
        """
        return self._score

    def getTarget(self) -> Location:
        """
        Get the location object that will be used as the click point.

        Typically, when no offset was specified by Pattern.targetOffset(),
        the click point is the center of the matched region. If an offset
        was given, the click point is the offset relative to the center.
        """
        return self.getCenter() + self._targetOffset

    def __lt__(self, other: 'Match'):
        return self.getScore() < other.getScore()

    def __repr__(self):
        return "%s(%r, %.3f)" % (
            self.__class__.__name__,
            self.getRect(), self.getScore()
        )
