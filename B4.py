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
    # 配列「weather_information」の中からキー「'temperature'」のバリューを取り出す。
    get_japan_temperature = [temperature.get('temperature') for temperature in weather_information]
    # print(get_japan_temperature)

    # 配列の要素数を数える
    count = len(weather_information)
    # print(count)

    # # 配列「weather_information」の和を配列の要素数で割る
    print(sum(get_japan_temperature) / count)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # 配列「oosaka」にキー「'prefecture'」が「'大阪府'」のものだけ取り出す。
    oosaka = [x for x in weather_information if x['prefecture'] == '大阪府']
    # print(oosaka)

    # 配列「oosaka」の中からキー「'station'」のバリューを取り出す。
    get_oosaka_station = [station.get('station') for station in oosaka]
    print(get_oosaka_station)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    # 配列「fukuoka」にキー「'prefecture'」が「'福岡県'」のものだけ取り出す。
    fukuoka = [x for x in weather_information if x['prefecture'] == '福岡県']
    # print(fukuoka)

    # 配列「fukuoka」の中からキー「'temperature'」のバリューを取り出す。
    get_fukuoka_temperature = [temperature.get('temperature') for temperature in fukuoka]
    # print(get_fukuoka_temperature)

    # 配列の要素数を数える
    count = len(get_fukuoka_temperature)
    # print(count)

    # 配列「get_fukuoka_temperature」の和を配列の要素数で割る
    print(sum(get_fukuoka_temperature) / count)


if __name__ == '__main__':
    main()
