import pytest

import demos.file_demos as fds

invalid_file_paths = ["", "/not/exist/file"]


@pytest.mark.parametrize("file_path", invalid_file_paths)
def test_fsplit_with_invalid_file(file_path):
    with pytest.raises(ValueError):
        fds.fsplit(file_path)


invalid_src_file_paths = [[], ["/only/one/file"], ["/not/exist/file1", "/not/exist/file2"]]


@pytest.mark.parametrize("src_file_paths", invalid_src_file_paths)
def test_fmerge_with_invalid_src_files(src_file_paths):
    with pytest.raises(ValueError):
        fds.fmerge(src_file_paths)


def test_fsplit_and_fmerge():
    fds.fsplit("./data/pg26184.txt", 500)
    fds.fmerge(["./pg26184.txt_0", "./pg26184.txt_1", "./pg26184.txt_2", "./pg26184.txt_3"], "pg26184.txt_merged")
    import filecmp

    assert filecmp.cmp("./data/pg26184.txt", "pg26184.txt_merged") is True
    fds.fsplit("./data/pg26184_1.txt", 400, "data.txt")
    fds.fmerge(["./data.txt_0", "./data.txt_1", "./data.txt_2", "./data.txt_3"], "data.txt_merged")
    assert filecmp.cmp("./data/pg26184_1.txt", "data.txt_merged") is True
