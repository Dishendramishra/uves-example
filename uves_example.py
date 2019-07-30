"""
Simple usage example for PyReduce
Loads a sample UVES dataset, and runs the full extraction
"""

import os.system
import os.path
import pyreduce
from pyreduce import datasets


# define parameters
instrument = "UVES"
target = "HD132205"
night = "2010-04-01"
mode = "middle"
steps = (
    "bias",
    "flat",
    "orders",
    # "norm_flat",
    # "wavecal",
    # "curvature",
    "science",
    # "continuum",
    "finalize",
)

# some basic settings
# Expected Folder Structure: base_dir/datasets/HD132205/*.fits.gz
# Feel free to change this to your own preference, values in curly brackets will be replaced with the actual values {}

# load dataset (and save the location)
base_dir = datasets.UVES_HD132205("./")
# base_dir =  "./"
input_dir = "{target}/"
output_dir = "reduced/{instrument}/{target}/{night}/{mode}"

config = os.path.join(os.path.dirname(__file__), "settings_UVES.json")

pyreduce.reduce.main(
    instrument,
    target,
    night,
    mode,
    steps,
    base_dir=base_dir,
    input_dir=input_dir,
    output_dir=output_dir,
    configuration=config,
    order_range=(1, 21),
)


def cleanup():
    os.system("rm -rf datasets pyreduce uves_data.tar.gz")

# cleanup()