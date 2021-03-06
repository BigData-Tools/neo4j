# -*- mode: Python; coding: utf-8 -*-

# Copyright (c) 2002-2011 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Neo4j is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python

from distutils.core import setup

with open('README.txt') as file:
  long_description = file.read()

setup(
    name='neo4j-embedded',
    
    # This is auto-generated by the 
    # maven build that runs this project
    version='${pythonic_version}', 
    
    description='Bindings for the embedded version of the neo4j graph database.',
    long_description=long_description,
    author='Neo Technology',
    author_email='python@neotechnology.com',
    
    url='https://github.com/neo4j/python-embedded',
    
    packages=(
        'neo4j',
        'neo4j.javalib',
    ),
    
    install_requires=(
      'setuptools',
    ),
    
    package_data = {
        # Include our java dependencies
        '': ['*.jar'],
    },
    
    classifiers=(
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Database :: Database Engines/Servers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Java',
    ),
)
