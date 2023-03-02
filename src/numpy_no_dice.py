import numpy
import argparse
import click
import sys

# From: https://blog.pantsbuild.org/packaging-python-with-the-pyoxidizer-pants-plugin/
# Patch missing sys.argv[0] which is None for some reason when using PyOxidizer
# Typer fails on this because it tries to emit the filename
if sys.argv[0] is None:
   sys.argv[0] = sys.executable

@click.command()
@click.option('--chicken-noodles/--no-chicken-noodles', default=False)
def main(chicken_noodles):
    if chicken_noodles:
        print("Like I said, I am a vegetarian\n")
        print(f"Digest these instead : {numpy.random.beta(3, 1, 10)}\n")
    else:
        print(f"Digest these : {numpy.random.beta(3, 1, 2)}\n")

if __name__ == "__main__":
    main()
