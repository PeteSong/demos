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


def _resolve_file_path(file_path: str) -> Path:
    p = Path(file_path).expanduser().resolve()
    return p
    # file_path = os.path.expanduser(file_path)
    # file_path = os.path.realpath(file_path)
    # return file_path


def fsplit_by_line_number(src_file_path: str, line_num: int = 1000, target_file_prefix: Optional[str] = None) -> None:
    """split file by line number"""

    def _write_split_file() -> None:
        target_file_path = f"{target_file_prefix}_{split_count}"
        # with newline="", the line terminators are written without translation.
        with open(target_file_path, "w", encoding="utf-8", newline="") as target_file:
            target_file.write(lines.getvalue())
        print(f"{target_file_path} created.")

    src_file_path = _resolve_file_path(src_file_path)
    if not os.path.isfile(src_file_path):
        raise ValueError(f"File not found or not a regular file: {src_file_path}")

    if target_file_prefix is None:
        target_file_prefix = os.path.basename(src_file_path)
    # with newline="", the line terminators are written without translation.
    with open(src_file_path, "r", encoding="utf-8", newline="") as src_file:
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
                lines.seek(0)
                lines.truncate(0)
        if line_count > 0:
            _write_split_file()


def fsplit_by_byte_size(src_file_path: str, size: int = 1024 * 1024, target_file_prefix: Optional[str] = None) -> None:
    """split file by size(bytes)"""
    src_file_path = _resolve_file_path(src_file_path)
    if not os.path.isfile(src_file_path):
        raise ValueError(f"File not found or not a regular file: {src_file_path}")

    if target_file_prefix is None:
        target_file_prefix = os.path.basename(src_file_path)
    # with newline="", the line terminators are written without translation.
    with open(src_file_path, "rb") as src_file:
        split_count = 0
        while trunk := src_file.read(size):
            target_file_path = f"{target_file_prefix}_b{split_count}"
            with open(target_file_path, "wb") as target_file:
                target_file.write(trunk)
            print(f"{target_file_path} created.")
            split_count += 1


def fmerge(src_file_paths: list[str], target_file_path: str = "target_merged_file") -> None:
    if len(src_file_paths) <= 1:
        raise ValueError("At least two source files are required.")

    paths = []
    for src_file_path in src_file_paths:
        p = Path(src_file_path).expanduser()
        if not p.is_file():
            raise ValueError(f"File not found or not a regular file: {src_file_path}")
        paths.append(p)
    with open(target_file_path, "wb") as target_file:
        for p in paths:
            with open(p, "rb") as src_file:
                target_file.write(src_file.read())
    print(f"{target_file_path} created.")


def fhash(src_file_path: str, hash_func: Callable) -> str:
    src_file_path = _resolve_file_path(src_file_path)
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


def fls(file_path: str) -> None:
    def _get_flag(_p: Path) -> str:
        if _p.is_symlink():
            return f"@ -> {_p.readlink()}"
        if _p.is_dir():
            return "/"
        return ""

    p = Path(file_path).expanduser()
    if not p.exists():
        print(f"File not found: {file_path}")
        return

    if p.is_file():
        print(f"{file_path} {_get_flag(p)}")
        return

    if p.is_dir():
        print(f"Files under {file_path}: \n")
        for child in p.iterdir():
            print(f"{child.name} {_get_flag(child)}")
        return


def fappend(file_path: str, content: str) -> None:
    with open(file_path, "a") as f:
        f.write(content)


def fappend2(file_path: str, content: str) -> None:
    with open(file_path, "r+") as f:
        f.seek(0, os.SEEK_END)
        f.write(content)


def fjoin_lines(in_file_path: str, out_file_path, sep=",", end=".") -> None:
    """join the lines with sep from in-file, write to out-file"""
    ifile_path = Path(in_file_path).expanduser()
    if not ifile_path.exists():
        raise ValueError(f"File not found or not a regular file: {in_file_path}")
    with open(ifile_path, "rb") as ifile:
        with open(out_file_path, "wb") as ofile:
            for line in ifile:
                ofile.write(line.strip(b"\n"))
                ofile.write(sep.encode())
            ofile.seek(-1, os.SEEK_CUR)
            ofile.write(end.encode())


def fgrep(file_path: str, target: str, displaying_line_number: bool = True):
    file_path = _resolve_file_path(file_path)
    if not os.path.isfile(file_path):
        raise ValueError(f"File not found or not a regular file: {file_path}")
    line_number = 0
    with open(file_path, "r") as f:
        for line in f:
            line_number += 1
            if target.casefold() in line.casefold():
                line = line.rstrip()
                if displaying_line_number:
                    l1 = f"{line_number} : {line}"
                else:
                    l1 = line
                print(l1)


def main() -> None:  # pragma: no cover
    fsplit_by_line_number("./data/pg26184.txt", 500)
    fmerge(["./pg26184.txt_0", "./pg26184.txt_1", "./pg26184.txt_2", "./pg26184.txt_3"], "pg26184.txt_merged")
    print(fmd5("./data/pg26184.txt"), fmd5("pg26184.txt_merged"))

    fsplit_by_byte_size("./data/pg26184.txt", 1024 * 20)
    fmerge(["./pg26184.txt_b0", "./pg26184.txt_b1", "./pg26184.txt_b2", "./pg26184.txt_b3"], "pg26184.txt_bmerged")
    print(fmd5("./data/pg26184.txt"), fmd5("pg26184.txt_bmerged"))


if __name__ == "__main__":
    # main()
    # fls('~')

    # fappend('../data/test_text.txt', 'hello world')
    # fmerge_lines("../data/test_text.txt", "../data/out_test_text.txt")
    fgrep("./data/pg26184.txt", "first")
