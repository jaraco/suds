#!/usr/bin/python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

# 'setuptools' related packages.
from setuptools import setup, find_packages


package_name = "suds-bis"
project_url = "https://github.com/jaraco/suds"


setup(
    name=package_name,
    description="Lightweight SOAP client",
    keywords=["SOAP", "web", "service", "client"],
    url=project_url,
    packages=find_packages(),

    # 'maintainer' will be listed as the distribution package author.
    # Warning: Due to a 'distribute' package defect when used with Python 3
    # (verified using 'distribute' package version 0.6.25), given strings must
    # be given using ASCII characters only. This is needed because 'distribute'
    # stores the strings by doing a simple write to a PKG-INFO file opened as a
    # 'default text file' thus attempting to encode the given characters using
    # the user's default system code-page, e.g. typically CP1250 on eastern
    # European Windows, CP1252 on western European Windows, UTF-8 on Linux or
    # any other.
    #
    # 'distribute' package merged back with the 'setuptools' package in the
    # setuptools 0.7 release but we have not yet checked whether this bug has
    # been corrected there or not.
    author="Jeff Ortel",
    author_email="jortel@redhat.com",
    maintainer="Jason R. Coombs",
    maintainer_email="jaraco@jaraco.com",

    #   See PEP-301 for the classifier specification. For a complete list of
    # available classifiers see
    # 'http://pypi.python.org/pypi?%3Aaction=list_classifiers'.
    classifiers=["Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
            "GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet"],
)
