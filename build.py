#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

import argparse
import json
import os
import shutil
import subprocess
import sys

__author__ = "Benjamin Kane"
__version__ = "0.1.0"
__doc__ = f"""
Build custom import site
Examples:
    {sys.argv[0]}
Help:
Please see Benjamin Kane for help.
"""


def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    return parser.parse_args(*args, **kwargs)


def main():
    _ = parse_args()

    # Change to script directory so I don't rmtree some other docs/
    file_dir = Path(__file__).parent
    os.chdir(file_dir)

    build_dir = Path("./docs/")
    site = "go.bbkane.com"
    vangen_config = "./vangen.json"

    shutil.rmtree(build_dir)
    subprocess.run(["vangen", f"-out={build_dir}"])

    Path(build_dir, "CNAME").write_text(site)

    with Path(vangen_config).open() as fp:
        config_data = json.load(fp)

    with Path(build_dir, "index.html").open("w") as fp:
        repos = [r for r in config_data["repositories"]]
        repos.sort(key=lambda r: r["prefix"])

        print("<h1>Packages</h1>", file=fp)
        print("<ul>", file=fp)

        for repo in repos:
            prefix = repo["prefix"]
            link = f'<a href="https://{site}/{prefix}">{prefix}</a>'
            print(f"<li>{link}</li>", file=fp)

        print("</ul>", file=fp)


if __name__ == "__main__":
    main()
