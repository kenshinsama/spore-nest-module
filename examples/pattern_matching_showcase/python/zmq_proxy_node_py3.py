#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess

subprocess.call([sys.executable, "zmq_proxy_node.py"]+sys.argv[1:])
