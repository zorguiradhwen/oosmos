#!/usr/bin/env python

import sys

sys.path.append('../../..')
import oosmos

oosmos.cLinux.Compile('main', 'main.c regtest.c reg.c prt.c')
