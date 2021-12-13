import json

dovydnyk = {
    100: "Бесарабський",
    200: "Житній",
    300: "Володимирський"
}
global_data = {
    "02.11.16;100;45;50;70",
    "02.11.16;200;35;30;50",
    "02.11.16;300;35;30;45",
    "14.11.2016;100;45;45;60",
    "14.11.2016;200;40;40;50",
    "14.11.2016;300;35;35;45",
    "22.11.2016;100;40;40;60",
    "22.11.2016;200;40;40;50",
    "22.11.2016;300;40;40;60"
}


class DataItem:
    def __init__(self, data: str):
        splitted = data.split(";")
        self.code = int(splitted[1])
        self.name = dovydnyk[self.code]
        self.date = splitted[0]
        self.p_1 = int(splitted[2])
        self.p_2 = int(splitted[3])
        self.p_3 = int(splitted[4])
        self.avg_price = (self.p_1 + self.p_2 + self.p_3) / 3

    def toString(self):
        return f"{self.code}\t{self.name}\t{self.date}\t{self.p_1}\t{self.p_2}\t{self.p_3}\t{self.avg_price}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def main():
    items = [DataItem(data) for data in global_data]
    for item in items:
        print(item.toString())
    write_to_file(items, "output.txt", 's')
    write_to_file(items, "output.json", 'json')


def write_to_file(data, filename, mode='s'):
    s = ''
    for item in data:
        s += f"{item.toString()}\n" if mode == 's' else item.toJSON()
    with open(filename, 'w+', encoding='utf-8') as file:
        file.write(s)


if __name__ == "__main__":
    main()
    