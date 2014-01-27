from ..api.repository import IRepository
from ..api.requirements import Requirement


class SimpleRepository(IRepository):
    def __init__(self, packages=None):
        #: :func:`set` of :class:`~versions.packages.Package` objects.
        self.packages = packages or set()

    def get(self, requirement):
        if isinstance(requirement, str):
            requirement = Requirement.parse(requirement)
        return (p for p in self.packages
                  if requirement.name == p.name and requirement.match(p))


class CompositeRepository(IRepository):
    """A composite repository.

    When querying a composite repository, it queries all repositories, and merges
    their results.

    :param repositories: Underlying package repositories.
    :type repositories: :func:`list` of :class:`Repository` or ``None``

    """
    def __init__(self, repositories=None):
        #: :func:`list` of :class:`Repository <repositories>`
        self.repositories = repositories or []

    def get(self, requirement):
        """Find packages matching ``requirement``.

        :param requirement: Requirement to get from all underlying \
        repositories.
        :type requirement: `str` or :class:`.Requirement`
        :returns: :class:`Iterator` of matching :class:`.Package` objects.

        """
        if isinstance(requirement, str):
            requirement = Requirement.parse(requirement)
        for repository in self.repositories:
            for package in repository.get(requirement):
                yield package
