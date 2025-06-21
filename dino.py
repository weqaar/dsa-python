import csv
import glob
import math


def read_csv_files(file_path):
    data = {}
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data[row["NAME"]] = row
    return data


def calculate_speed(stride_length, leg_length):
    g = 9.8  # gravitational constant
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)


def main():
    # Read data from CSV files
    dataset1 = read_csv_files("dataset1.csv")
    dataset2 = read_csv_files("dataset2.csv")

    # Calculate speed for bipedal dinosaurs
    speeds = {}
    for name, data in dataset2.items():
        if data["STANCE"] == "bipedal":
            leg_length = float(dataset1[name]["LEG_LENGTH"])
            stride_length = float(data["STRIDE_LENGTH"])
            speed = calculate_speed(stride_length, leg_length)
            speeds[name] = speed

    # Sort dinosaurs by speed from fastest to slowest
    sorted_dinos = sorted(speeds.items(), key=lambda x: x[1], reverse=True)

    # Print the names of the bipedal dinosaurs
    for dino in sorted_dinos:
        print(dino[0])


if __name__ == "__main__":
    main()
