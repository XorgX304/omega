#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Omega Framework                                
#            ---------------------------------------------------
#                  Copyright (C) <2020>  <Entynetproject>       
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import codecs


try:
    codecs.lookup("utf-8")
    default_encoding = "utf-8"
except LookupError:
    default_encoding = sys.getdefaultencoding()

try:
    codecs.lookup_error("surrogateescape")
    default_errors = "surrogateescape"
except LookupError:
    default_errors = "strict"


def encode(str_obj, encoding=default_encoding, errors=default_errors):
    """Encode the given bytes object with `encoding` encoder
    and `errors` error handler.
    If not set, `encoding` defaults to module's `default_encoding` variable.
    If not set, `errors` defaults to module's `default_errors` variable.
    """
    bytes_obj = str_obj.encode(encoding, errors)
    return bytes_obj


def decode(bytes_obj, encoding=default_encoding, errors=default_errors):
    """Decode the given bytes object with `encoding` decoder
    and `errors` error handler.
    If not set, `encoding` defaults to module's `default_encoding` variable.
    If not set, `errors` defaults to module's `default_errors` variable.
    """
    str_obj = bytes_obj.decode(encoding, errors)
    return str_obj
