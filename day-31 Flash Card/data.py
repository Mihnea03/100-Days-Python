import pandas

DATA_FILENAME = "words.csv"
OUT = "missed_words.csv"

def get_data():
    df = pandas.read_csv(DATA_FILENAME)
    data = [{"french": row.french, "english": row.english} for (_, row) in df.iterrows()]
    return data

def write_missed_words(data):
    new_dict = {
        "French": [],
        "English": []
    }
    print(len(data))

    new_dict["French"] = [word["french"] for word in data]
    new_dict["English"] = [word["english"] for word in data]

    df = pandas.DataFrame(new_dict)
    df.to_csv(OUT)