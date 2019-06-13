#!/bin/bash
echo "setting path variable"
export PATH=$PATH:<PATH_of_geckodriver>
echo "logging in to network"
python3 script.py
