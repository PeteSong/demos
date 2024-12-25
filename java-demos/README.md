## Setup Java environment on macOS

First install [SDK MAN](https://sdkman.io/install/)

Then install `java` and `gradle`

```shell
sdk install java 21.0.5-amzn
sdk install gradle 8.10.2
```

Then create gradle project

```shell
mkdir java-demos
cd java-demos

gradle init
```

Then create gradle wrapper
```shell
gradle wrapper
```

after then, we can use wrapper `./gradlew` to build project

## Run a file

```shell
./gradlew clean
./gradlew build

./gradlew runClass -PclassName=io.petesong.leetcode.LeetCode2235
```

## Check before commit

```shell
./gradlew check
```
Then you can see the reports after checking in the folder `./build/reports`
