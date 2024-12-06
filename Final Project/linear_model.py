import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os


class LinearModel():
    def __init__ (self):
        self.model = LinearRegression()
        self.x = None
        self.yvar = None
        self.original_data_path = "LinearModelData.csv"
        self.database_path = "PressureSensorData.csv"

        self.setup_model()
        
    def setup_model(self):
        #print("Loading in Dataset...")
        if os.path.exists("LinearModelData.csv"):
            self.load_dataset(self.database_path)
        else:
            self.load_dataset(self.original_data_path)

        print("Training model...")
        self.train()

        print("Model ready to be used \n")

    def load_dataset(self, filepath):
        print(f"\nLoading in the Dataset from {filepath}... \n")
        self.sensor_data = pd.read_csv(filepath)
        self.sensor_data = self.sensor_data[["test_id", "pt_psia", "pd_volts"]] # only get needed columns

        self.sensor_data.rename(columns = {"pt_psia": "actual","pd_volts": "transducer"}, inplace = True)
        self.sensor_data.to_csv("LinearModelData.csv")
        print("Dataset successfully loaded.\n")

    def append_dataset(self):
        # create interface to enter values
        test_id = input("\ninput a test id")

        actual = input("Please input the actual pressure")
        while not actual.replace(".", "").isnumeric():
            print("Please enter a integer value")
            actual = input("Please input the actual pressure")
        actual = float(actual)


        voltage = input("Please input the measured Transducer Voltage")
        while not voltage.replace(".", "").isnumeric():
            print("Please enter a integer value")
            voltage = input("Please input the measured Transducer Voltage")
        voltage = float(voltage)

        print(f"You inputed: test id: {test_id}, actual pressure: {actual}, and transducer voltage: {voltage}.")

        decision = input("Do you want to input this into the database? (y/n)")

        if decision.lower() in ["y","yes"]:
            new_readings = {"test_id": test_id, "actual": actual, "transducer": voltage}
            self.sensor_data = pd.concat([self.sensor_data, pd.DataFrame([new_readings])], ignore_index=True)
            self.sensor_data.to_csv("LinearModelData.csv")
            print("Entries entered into the database.\n")
        else:
            print("Entries were not entered into the database.\n")


    def split_data (self):
        pass


    def train (self):
        #splitting data
        X = self.sensor_data[["transducer"]]
        y = self.sensor_data["actual"]

        # using a 80 - 20 split for the data - no use for test data
        #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

        self.model.fit(X,y) # no use excluding any data for test. Note evaluating model anyway

    def predict (self):
        voltage = input("\nPlease input a voltage to predict a value")
        while not voltage.replace(".", "").isnumeric():
            print("Please enter a integer value")
            voltage = input("Please input a voltage to predict a value")
        voltage = float(voltage)

        pressure = self.model.predict([[voltage]])[0]
        print(f"The predicted pressure is {round(pressure, 2)}\n")

    def retrain (self, **args):
        print("Retraining model with updated parameters...")
        self.train(**args)
        print("Done! \n")
        
    def interface(self):
        command = None
        commands = ["exit", "retrain", "update", "predict","load", "reload"]
        command_destinations = {
            "exit": None,
            "retrain": self.retrain,
            "update": self.append_dataset,
            "predict": self.predict,
            "load": lambda: self.load_dataset(self.database_path),
            "reload": lambda: self.load_dataset(self.original_data_path)
            }

        
        print("This is your Linear Model Interface!\n")


        while command != "exit":
            command = input(f"Choose one of the following commands: {", ".join(commands)}: ")
            while command not in commands:
                command = input(f"Choose one of the following commands: {", ".join(commands)}: ")
            if command == "exit":
                break
            else:
                command_destinations[command]()


        print("All data saved. Terminating")