import pandas
data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")


grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])


black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])



squirrel_count_dict = {
    "fur color" : ["Grey", "Black", "Red"],
    "count" : [grey_squirrels_count, black_squirrels_count, red_squirrels_count]
}

squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count.csv")
