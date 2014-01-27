import abc
from .requirements import Requirement


class IRepository(object):
    """A package repository.
    
    :param packages: Repository packages.
    :type packages: :func:`set` of :class:`.Package` or `None`

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, requirement):
        """Find packages matching ``requirement``.

        :param requirement: Requirement to match against repository packages.
        :type requirement: `str` or :class:`.Requirement`
        :returns: :class:`Iterable` of matching :class:`.Package` objects.

        """
        return

