#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__description__ = \
    """
A small script to generate a json file to assign genders to a list of first names...
NB. Written for python 3, not tested under 2.
"""
__author__ = "Matteo Ferla. [Github](https://github.com/matteoferla)"
__email__ = "matteo.ferla@gmail.com"
__date__ = ""
__license__ = "Cite me!"
__version__ = "1.0"

import urllib.request
from collections import defaultdict
import json


class Gender():
    """
    g.male=prevalence out of 1/2 377000
    g.female=prevalence
    g.common() = most common
    g.diff() = % og that...
    """
    epsilon=1/377001
    def __init__(self,gender='male',value=epsilon):
        self.male=self.epsilon
        self.female=self.epsilon
        setattr(self,gender,value)
    def __setitem__(self,key,value):
        setattr(self,key,float(value))
    def __getitem__(self,key):
        getattr(self,key)
    def __str__(self):
        return 'male: {m:.2}, female: {f:.2}'.format(m=self.male,f=self.female)
    def common(self):
        return 'male' if self.male>self.female else 'female'
    def diff(self):
        tally=self.male+self.female
        return (self.male/tally)*100 if self.male>self.female else (self.female/tally)*100

if __name__ == "__main__":
    genderdex = defaultdict(Gender)
    for sex in ('male', 'female'):
        url = 'http://deron.meranda.us/data/census-dist-{}-first.txt'.format(sex)
        text = urllib.request.urlopen(url).read().decode('utf-8')
        for row in text.split('\n'):
            if row:
                name = row.split()
                genderdex[name[0].title()][sex] = name[1]

    json.dump([(name, genderdex[name].common(), genderdex[name].diff()) for name in genderdex],
              open('gender.json', 'w'))