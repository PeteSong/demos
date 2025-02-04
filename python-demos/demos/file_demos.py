"""
Model Name: file_demos.py
Description: file demos
Author: Peter Song
Date: 2025-01-11
Version: 0.0.1
"""

import hashlib
import io
import os
from collections.abc import Callable
from functools import partial
from pathlib import Path
from typing import Optional


def fsplit(src_file_path: str, line_num: int = 1000, target_file_prefix: Optional[str] = None) -> None:
    def _write_split_file() -> None:
        target_file_path = f"{target_file_prefix}_{split_count}"
        # with newline="", the line terminators are written without translation.
        with open(target_file_path, "w", encoding="utf-8", newline="") as target_file:
            target_file.write(lines.getvalue())
        print(f"{target_file_path} created.")
        lines.close()

    src_file_path = os.path.expanduser(src_file_path)
    if not os.path.isfile(src_file_path):
        raise ValueError(f"File not found or not a regular file: {src_file_path}")
    if target_file_prefix is None:
        target_file_prefix = os.path.basename(src_file_path)
    # with newline="", the line terminators are written without translation.
    with open(src_file_path, encoding="utf-8", newline="") as src_file:
        line_count = 0
        # with newline="", the line terminators are written without translation.
        lines = io.StringIO(newline="")
        split_count = 0
        for line in src_file:
            lines.write(line)
            line_count += 1
            if line_count == line_num:
                _write_split_file()
                split_count += 1
                line_count = 0
                lines = io.StringIO()
        if line_count > 0:
            _write_split_file()


def fmerge(src_file_paths: list[str], target_file_path: str = "target_merged_file") -> None:
    if len(src_file_paths) <= 1:
        raise ValueError("At least two source files are required.")
    paths = []
    for src_file_path in src_file_paths:
        p = Path(src_file_path).expanduser()
        if not p.is_file():
            raise ValueError(f"File not found or not a regular file: {src_file_path}")
        paths.append(p)
    # with newline="", the line terminators are written without translation.
    with open(target_file_path, "w", encoding="utf-8", newline="") as target_file:
        for p in paths:
            # with newline="", the line terminators are written without translation.
            with open(p, encoding="utf-8", newline="") as src_file:
                target_file.write(src_file.read())
    print(f"{target_file_path} created.")


def fhash(src_file_path: str, hash_func: Callable) -> str:
    src_file_path = os.path.expanduser(src_file_path)
    if not os.path.isfile(src_file_path):
        raise ValueError(f"File not found or not a regular file: {src_file_path}")
    CHUNK_SIZE_OF_BYTES = 4096
    with open(src_file_path, "rb") as src_file:
        h = hash_func()
        for chunk in iter(partial(src_file.read, CHUNK_SIZE_OF_BYTES), b""):
            h.update(chunk)
    return h.hexdigest()


def fmd5(src_file_path: str) -> str:
    hexdigest = fhash(src_file_path, hashlib.md5)
    print(f"MD5({src_file_path}) = {hexdigest}")
    return hexdigest


def main() -> None:  # pragma: no cover
    fsplit("./data/pg26184.txt", 500)
    fmerge(["./pg26184.txt_0", "./pg26184.txt_1", "./pg26184.txt_2", "./pg26184.txt_3"], "pg26184.txt_merged")
    print(fmd5("./data/pg26184.txt"))


if __name__ == "__main__":
    # main()
    print(fmd5("./data/pg26184.txt"))
