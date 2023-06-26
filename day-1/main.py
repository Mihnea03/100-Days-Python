# Band Name Generator
# Munteanu Mihnea @ Stephan03

def main():
    print("Welcome to the Band Name Generator.")

    print("What's the name of the city you grew up in?")
    city_name = str(input())
    print("What's your pet's name?")
    pet_name = str(input())

    band_name = city_name +' ' + pet_name

    print("Your band name could be {}".format(band_name))

if __name__ == '__main__':
    main()