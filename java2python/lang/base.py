#!/usr/bin/env python
# -*- coding: utf-8 -*-
# java2python.lang.base -> lexer and parser support classes.
#
# This module provides the following:
#
# * `Tokens`
#
# This class is used to create the single `token` instance in this
# module.  It is used to map between parser tokens and their ids and
# vice-versa.


# ANTLR notes:
#
# recognizers: lexer, parser, treeparser
# streams: string, file name, file handle
#
# Parsers use TokenStreams (CommonTokenStream or TokenRewriteStream)
#
# Tree parsers use TreeNodeStream (CommonTreeNodeStream)
#
# Lexers emit Token objects (buffered in TokenStream objects)
#
# Parsers build trees if their output is AST.
#
# token types: CommonToken and ClassicToken.  Our tree adaptor
# creates LocalTree instances instead.
#
# Tree (CommonTree) wraps Token objects.  We provide extra functionality via
# the LocalTree class.
#
# TreeAdaptor (CommonTreeAdaptor) is used by the parser to create
# Tree objects.  Our adaptor, TreeAdaptor, creates the LocalTree
# instances.
#

from io import StringIO

from antlr4 import CommonTokenStream as TokenStream

from java2python.lib import colors


class Tokens(object):
    """ Tokens -> simplifies token id-name and name-id mapping. """

    def __init__(self):
        self.cache, self.parserModule = {}, None

    def __getattr__(self, name):
        """ tokenname -> tokenvalue """
        return getattr(self.module, name)

    @property
    def commentTypes(self):
        """ Well-known comment types. """
        mod = self.module
        return (mod.COMMENT, mod.LINE_COMMENT, mod.JAVADOC_COMMENT, )

    @property
    def map(self):
        """ (tokentype, tokenname) mapping as a dictionary """
        cache, module = self.cache, self.module
        if cache:
            return cache
        mapping = [(getattr(module, k, None), k) for k in module.tokenNames]
        mapping = [(k, v) for k, v in mapping if k is not None]
        cache.update(mapping)
        return cache

    @property
    def methodTypes(self):
        """ Well-known method types. """
        mod = self.module
        return (mod.VOID_METHOD_DECL, mod.FUNCTION_METHOD_DECL, )

    @property
    def primitiveTypeNames(self):
        """ Type name of well-known primitive types """
        return ('bool', 'str', 'int', 'long', 'float', )

    @property
    def module(self):
        """ Provides lazy import to the parser module. """
        module = self.parserModule
        if module:
            return module
        import java2python.lang.JavaParser as module
        self.parserModule = module
        return module

    @staticmethod
    def title(name):
        """ Returns a nice title given a token type name. """
        return ''.join(part.title() for part in name.split('_'))


## sometimes you really do only need one.
tokens = Tokens()
