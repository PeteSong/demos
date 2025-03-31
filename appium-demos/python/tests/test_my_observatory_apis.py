from apis.my_observatory_apis import get_nine_day_data_from_open_api, get_nine_day_data_from_pda_api


def test_get_nine_day_data_from_open_api():
    data = get_nine_day_data_from_open_api()
    assert data is not None
    assert len(data) == 9


def test_get_nine_day_data_from_pda_api():
    data = get_nine_day_data_from_pda_api()
    assert data is not None
    assert len(data) == 9
