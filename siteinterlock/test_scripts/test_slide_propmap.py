# Sebastian Raschka 2016
#
# `siteinterlock` is a Python package for selecting near-native protein-ligand
# docking poses based upon the hypothesis that interfacial rigidification
# of both the protein and ligand prove to be important characteristics of
# the native binding mode and are sensitive to the spatial coupling of
# interactions and bond-rotational degrees of freedom in the interface.
#
# Copyright (C) 2016 Michigan State University
# License: GPLv3
#
# SiteInterlock was developed in the
# Protein Structural Analysis & Design Laboratory
# (http://www.kuhnlab.bmb.msu.edu)
# Contact email: kuhnlab@msu.edu
#
# Package author: Sebastian Raschka <http://sebastianraschka.com>
#


import os
import subprocess
import shutil


absdir = os.path.dirname(os.path.abspath(__file__))


def test_propmap():

    s_path = os.path.join('..', '..',
                          'scripts', 'slide_propmap.py')
    e1_path = os.path.join('..', '..',
                           'examples', 'slide-propmap',
                           '1com_crystal.mol2')
    e2_path = os.path.join('..', '..',
                           'examples', 'slide-propmap',
                           '1com_0.pts')

    abs_script = os.path.join(absdir, s_path)
    abs1_examples = os.path.join(absdir, e1_path)
    abs2_examples = os.path.join(absdir, e2_path)

    r = subprocess.Popen(['python', abs_script,
                          '--input1', abs1_examples,
                          '--input2', abs2_examples],
                         stdout=subprocess.PIPE).communicate()[0]

    r = [i for i in r.decode("utf-8").split('\n')]
    r = [i for i in r if i and not i.startswith('#')]
    expect = ['================', 'PROPMAP results',
              '================', 'C1 --> hydrophobic contact',
              'C3 --> hydrophobic contact', 'C5 --> hydrophobic contact',
              'C8 --> hydrophobic contact',
              'O1 --> b [H-bond Donor and/or Acceptor]',
              'O2 --> a [H-bond Acceptor]',
              'O3 --> a [H-bond Acceptor]',
              'O4 --> a [H-bond Acceptor]',
              'O5 --> a [H-bond Acceptor]',
              'O6 --> a [H-bond Acceptor]']

    assert r == expect, r
