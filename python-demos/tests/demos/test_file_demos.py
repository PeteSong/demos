import filecmp

import pytest

import demos.file_demos as fds

invalid_file_paths = ["", "/not/exist/file"]


@pytest.mark.parametrize("file_path", invalid_file_paths)
def test_fsplit_with_invalid_file(file_path):
    with pytest.raises(ValueError):
        fds.fsplit_by_line_number(file_path)
    with pytest.raises(ValueError):
        fds.fsplit_by_byte_size(file_path)


invalid_src_file_paths = [[], ["/only/one/file"], ["/not/exist/file1", "/not/exist/file2"]]


@pytest.mark.parametrize("src_file_paths", invalid_src_file_paths)
def test_fmerge_with_invalid_src_files(src_file_paths):
    with pytest.raises(ValueError):
        fds.fmerge(src_file_paths)


def test_fsplit_and_fmerge():
    fds.fsplit_by_line_number("./data/pg26184.txt", 500)
    fds.fmerge(["./pg26184.txt_0", "./pg26184.txt_1", "./pg26184.txt_2", "./pg26184.txt_3"], "pg26184.txt_merged")

    assert filecmp.cmp("./data/pg26184.txt", "pg26184.txt_merged") is True
    fds.fsplit_by_line_number("./data/pg26184_1.txt", 400, "data.txt")
    fds.fmerge(["./data.txt_0", "./data.txt_1", "./data.txt_2", "./data.txt_3"], "data.txt_merged")
    assert filecmp.cmp("./data/pg26184_1.txt", "data.txt_merged") is True


def test_fsplit_and_fmerge_with_tmp_path(tmp_path):
    d = tmp_path / "test_fsplit_and_fmerge_with_tmp_path"
    d.mkdir()
    target_file_prefix = d / "test_data.txt"
    src_file_path = "./data/pg26184.txt"
    fds.fsplit_by_line_number(src_file_path, 500, target_file_prefix=target_file_prefix)

    splited_file_paths = sorted([str(d / child) for child in d.iterdir()])
    target_file_path = str(d / "test_data.txt_merged")
    fds.fmerge(splited_file_paths, target_file_path)

    assert filecmp.cmp(src_file_path, target_file_path) is True


def test_fsplit2_and_fmerge_with_tmp_path(tmp_path):
    d = tmp_path / "test_fsplit2_and_fmerge_with_tmp_path"
    d.mkdir()
    target_file_prefix = d / "test_data.txt"
    src_file_path = "./data/pg26184.txt"
    fds.fsplit_by_byte_size(src_file_path, 1024 * 10, target_file_prefix=target_file_prefix)

    splited_file_paths = sorted([str(d / child) for child in d.iterdir()])
    target_file_path = str(d / "test_data.txt_merged")
    fds.fmerge(splited_file_paths, target_file_path)

    assert filecmp.cmp(src_file_path, target_file_path) is True


def test_fsplit2_and_fmerge():
    src_file_path = "./data/pg26184.txt"
    fds.fsplit_by_byte_size(src_file_path, 1024 * 20)

    splited_file_paths = ["pg26184.txt_b0", "pg26184.txt_b1", "pg26184.txt_b2", "pg26184.txt_b3"]
    fds.fmerge(splited_file_paths)

    assert filecmp.cmp(src_file_path, "target_merged_file") is True


@pytest.mark.parametrize("file_path", invalid_file_paths)
def test_fmd5_with_invalid_file(file_path):
    with pytest.raises(ValueError):
        fds.fmd5(file_path)


def test_fmd5():
    expected_md5 = "e8834a096fd0321ec195899959eb163f"
    actual_md5 = fds.fmd5("./data/pg26184.txt")
    assert actual_md5 == expected_md5
