from unittest import TestCase

from versions.contrib import SimpleRepository, CompositeRepository
from versions import Package

class TestRepository(TestCase):
    def test(self):
        packages = set([
            Package.parse('foo-1.0'),
            Package.parse('foo-2.0'),
            Package.parse('foo-3.0'),
            Package.parse('vim-7.4+perl.python'),
            Package.parse('vim-7.4+perl.ruby.python'),
            Package.parse('vim-6.0+perl.ruby.python'),
        ])
        repository = SimpleRepository(packages)
        self.assertEqual(len(set(repository.get('foo')) - set([
            Package.parse('foo-1.0'),
            Package.parse('foo-2.0'),
            Package.parse('foo-3.0'),
        ])), 0)
        self.assertEqual(len(set(repository.get('vim[ruby]>7')) - set([
            Package.parse('vim-7.4+perl.ruby.python')
        ])), 0)

class TestCompositeRepository(TestCase):
    def test(self):
        foo_repo = SimpleRepository([
            Package.parse('foo-1.0'),
            Package.parse('foo-2.0'),
            Package.parse('foo-3.0')])
        vim_repo = SimpleRepository([
            Package.parse('vim-7.4+perl.python'),
            Package.parse('vim-7.4+perl.ruby.python'),
            Package.parse('vim-6.0+perl.ruby.python')])
        crep = CompositeRepository([foo_repo, vim_repo])
        self.assertEqual(len(set(crep.get('foo')) - set([
            Package.parse('foo-1.0'),
            Package.parse('foo-2.0'),
            Package.parse('foo-3.0')
        ])), 0)
        self.assertEqual(len(set(crep.get('vim[ruby]>7')) - set([
            Package.parse('vim-7.4+perl.ruby.python')
        ])), 0)

