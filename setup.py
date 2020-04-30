#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# (c) 2017 SENAI CIMATEC/ITV.
#
# This file is part of Geonosis systems.
#
#

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    package_dir={'': 'src'},
    requires=['rospy', ' std_msgs','diagnostic_msgs']
)

setup(**d)
