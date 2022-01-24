def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # 「weather_information」配列の中のキー「temperature」を持った値を取り出す
    get_temperature_information = [temperature.get('temperature') for temperature in weather_information]
    print(get_temperature_information)

    # 配列の要素数を数える
    count = len(weather_information)
    print(count)

    # 「get_weather_information」配列の和を配列の要素数で割る
    print(sum(get_temperature_information) / count)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # prefecture = list.sort(weather_information, key='prefecture', values='大阪府')
    # print(prefecture)
    for x in weather_information:
        print(x)
        if (prefecture.get('prefecture') for prefecture in weather_information) == '大阪府':
            get_station_information = [station.get('station') for station in weather_information]
            return get_station_information

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


if __name__ == '__main__':
    main()
