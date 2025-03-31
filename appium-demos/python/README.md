# Setup
1. Setup the `Node.js` in MacOS ([link](https://petesong.github.io/macos/node.js/2025/02/21/setup-nodejs-environment-on-macOS.html)), install the `appium` and setup it.

2. Create an Android emulator(Android 12 with Google Play) in the Android Studio

3. Install [MyObservatory](https://play.google.com/store/apps/details?id=hko.MyObservatory_v1_0&hl=en) from Play Store into Android emulator. Also make sure the app icon is in the first screen.

## Optional

### trying to find the API endpoint of MyObservatory app by capturing the network traffic

1. Root the emulator with [rootAVD](https://gitlab.com/newbit/rootAVD)
2. Use `mitmproxy` to capture the API endpoint of MyObservatory app

Failed to capture the network traffic of MyObservatory app, so I have to decompile the apk to find the API endpoint.

### De-compile the apk to find the API endpoint of MyObservatory app
1. first pull the apk from the emulator
    ```shell
    # get the package name
    adb shell pm list package | grep -i observatory
    # get the apk file path
    adb shell pm path hko.MyObservatory_v1_0
    # pull the apk file
    adb pull /data/app/~~u8OxPu-IfonNLn_1TFvlJg==/hko.MyObservatory_v1_0-JHOrFC3r2YTG3VjqS1G4tA==/base.apk ~/tmp/myobservatory.apk
    ```
2. install `apktool`
   ```shell
   brew install apktool
   ```
3. decompile the apk
   ```shell
   apktool d ~/tmp/myobservatory.apk
   ```
4. search 'fnd' in the decompiled folder (`fnd` is from the [HKO Open data API Documentation](https://www.hko.gov.hk/tc/weatherAPI/doc/files/HKO_Open_Data_API_Documentation_tc.pdf))
   ```
   4592:    <string name="n_day_data_link_en">https://pda.weather.gov.hk/locspc/android_data/fnd_e.xml</string>
   4593:    <string name="n_day_data_link_sc">https://pda.weather.gov.hk/sc/locspc/android_data/fnd_uc.xml</string>
   4594:    <string name="n_day_data_link_tc">https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml</string>
   ```
# run test

## using `uv`
Run all test
```shell
uv run pytest
```

Run one test
```shell
uv run pytest ./tests/test_my_observatory_page.py
```

## using `pytest` directly
If you want to see the output in the stdout, use the `pytest -s`
```shell
# activate the venv
source .venv/bin/activate

pytest -s

# or

pytest -s ./tests/test_my_observatory_page.py
```
# reference
1. [HKO Open data API Documentation](https://www.hko.gov.hk/tc/weatherAPI/doc/files/HKO_Open_Data_API_Documentation_tc.pdf)
