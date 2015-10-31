#!/bin/bash

PYTHONPATH=$PYTHONPATH:~/nsc-site/:~/pydozer/  python ~/pydozer/pydozer.py --conf nsc_config.py --build
cp -av generated/* /var/www/nsc/
