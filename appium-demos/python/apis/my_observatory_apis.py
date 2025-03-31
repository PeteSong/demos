import requests

from pages.date_utils import get_next_day_labels


def get_nine_day_data_from_open_api():
    # url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en"
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    params = {"dataType": "fnd", "lang": "en"}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        data = data.get("weatherForecast", [])
        return data

    except requests.RequestException as e:
        print(f"Error fetching data from Open API: {e}")
        return None


def get_nine_day_data_from_pda_api():
    n_day_data_link_en = "https://pda.weather.gov.hk/locspc/android_data/fnd_e.xml"
    # n_day_data_link_sc = "https://pda.weather.gov.hk/sc/locspc/android_data/fnd_uc.xml"
    # n_day_data_link_tc = "https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml"
    url = n_day_data_link_en
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        data = data.get("forecast_detail", [])
        return data

    except requests.RequestException as e:
        print(f"Error fetching data from PDA API: {e}")
        return None


if __name__ == "__main__":
    day_labels = get_next_day_labels(fmt="%Y%m%d")

    for one_day in get_nine_day_data_from_open_api():
        # extract the relative humidity for the day after tomorrow
        if (date_label := one_day.get("forecastDate", "")) == day_labels[1]:
            min_rh = one_day.get("forecastMinrh", "").get("value", "")
            max_rh = one_day.get("forecastMaxrh", "").get("value", "")
            print(f"{date_label}: {min_rh} - {max_rh}% ")

    for one_day in get_nine_day_data_from_pda_api():
        # extract the relative humidity for the day after tomorrow
        if (date_label := one_day.get("forecast_date", "")) == day_labels[1]:
            min_rh = one_day.get("min_rh", "")
            max_rh = one_day.get("max_rh", "")
            print(f"{date_label}: {min_rh} - {max_rh}% ")
