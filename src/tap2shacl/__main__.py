#!/usr/bin/env python
from . import (
    TAP2SHACLConverter,
    __version__,
)
from .parseArguments import parse_arguments


def main():
    args = parse_arguments()
    print(args.tapFileName)
    tapFName = args.tapFileName
    c = TAP2SHACLConverter(tapFName, args.configFileName)
    c.convertTAP2AP(args.namespaceFileName, args.aboutFileName, args.shapesFileName)
    c.convertAP2SHACL()
    #    c.dump_ap()
    c.dump_shacl(args.outputFileName)


if __name__ == "__main__":
    print(__version__)
    main()
