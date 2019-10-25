"""
# Smart AST

Provides compatibility between AST 2 and 3.
"""
import os
from typing import Any

if os.environ.get("PYTHON_VER", "3") == "3":
    from typed_ast.ast3 import (  # pylint: disable=no-name-in-module
        Add,
        alias,
        And,
        arg,
        arguments,
        Assign,
        AST,
        Attribute,
        BinOp,
        BitAnd,
        BitOr,
        BitXor,
        BoolOp,
        Bytes,
        Call,
        ClassDef,
        Compare,
        Dict,
        Div,
        Ellipsis as ASTEllipsis,
        Eq,
        expr,
        FloorDiv,
        FunctionDef,
        get_docstring,
        Gt,
        GtE,
        Import,
        ImportFrom,
        In,
        Index,
        Invert,
        Is,
        IsNot,
        keyword,
        Lambda,
        List,
        LShift,
        Lt,
        LtE,
        Mod,
        Mult,
        Name,
        NameConstant,
        NodeVisitor,
        Not,
        NotEq,
        NotIn,
        Num,
        Or,
        parse,
        Pow,
        RShift,
        Set,
        Starred,
        stmt,
        Str,
        Sub,
        Subscript,
        Tuple,
        UAdd,
        UnaryOp,
        USub,
    )
else:
    from typed_ast.ast27 import (  # pylint: disable=no-name-in-module
        Add,
        alias,
        And,
        arguments,
        Assign,
        AST,
        Attribute,
        BinOp,
        BitAnd,
        BitOr,
        BitXor,
        BoolOp,
        Call,
        ClassDef,
        Compare,
        Dict,
        Div,
        Ellipsis as ASTEllipsis,
        Eq,
        expr,
        FloorDiv,
        FunctionDef,
        get_docstring,
        Gt,
        GtE,
        Import,
        ImportFrom,
        In,
        Index,
        Invert,
        Is,
        IsNot,
        keyword,
        Lambda,
        List,
        LShift,
        Lt,
        LtE,
        Mod,
        Mult,
        Name,
        NodeVisitor,
        Not,
        NotEq,
        NotIn,
        Num,
        Or,
        parse,
        Pow,
        RShift,
        Set,
        stmt,
        Str,
        Sub,
        Subscript,
        Tuple,
        UAdd,
        UnaryOp,
        USub,
    )

    arg = Any
    Bytes = Any
    NameConstant = Any
    Starred = Any

__all__ = [
    "Add",
    "alias",
    "And",
    "arg",
    "arguments",
    "Assign",
    "AST",
    "Attribute",
    "BinOp",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolOp",
    "Bytes",
    "Call",
    "ClassDef",
    "Compare",
    "Dict",
    "Div",
    "ASTEllipsis",
    "Eq",
    "expr",
    "FloorDiv",
    "FunctionDef",
    "get_docstring",
    "Gt",
    "GtE",
    "Import",
    "ImportFrom",
    "In",
    "Index",
    "Invert",
    "Is",
    "IsNot",
    "keyword",
    "Lambda",
    "List",
    "LShift",
    "Lt",
    "LtE",
    "Mod",
    "Mult",
    "Name",
    "NameConstant",
    "NodeVisitor",
    "Not",
    "NotEq",
    "NotIn",
    "Num",
    "Or",
    "parse",
    "Pow",
    "RShift",
    "Set",
    "Starred",
    "stmt",
    "Str",
    "Sub",
    "Subscript",
    "Tuple",
    "UAdd",
    "UnaryOp",
    "USub",
]
