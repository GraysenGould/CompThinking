import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os


class PressureSensorInterface():
    def __init__ (self):

        # initialize model to be used
        self.model = LinearRegression()

        self.original_data_path = "PressureSensorData.csv"
        self.database_path = "LinearModelData.csv"
        
        self.setup_model()
        
    def setup_model(self):
        # load correct dataset
        if os.path.exists("LinearModelData.csv"):
            self.load_dataset(self.database_path)
        else:
            self.load_dataset(self.original_data_path)

        #initial training of model
        print("Training model...")
        self.train()
        print("Model ready to be used \n")

    def load_dataset(self, filepath):
        print(f"\nLoading in the Dataset from {filepath}... \n")
        self.sensor_data = pd.read_csv(filepath)
        
        # only rename columns if using original data
        if filepath == self.original_data_path:
            self.sensor_data.rename(columns = {"pt_psia": "actual","pd_volts": "transducer"}, inplace = True)

        # select three columns needed
        self.sensor_data = self.sensor_data[["test_id", "actual", "transducer"]] # only get needed columns

        # save data to database
        self.sensor_data.to_csv("LinearModelData.csv")
        print("Dataset successfully loaded.\n")

    def append_dataset(self):
        # get test id
        test_id = input("\ninput a test id")

        # get actual pressure
        actual = input("Please input the actual pressure")
        while not actual.replace(".", "").isnumeric():
            print("Please enter a numerical value")
            actual = input("Please input the actual pressure")
        actual = float(actual)

        # get transducer voltage
        voltage = input("Please input the measured Transducer Voltage")
        while not voltage.replace(".", "").isnumeric():
            print("Please enter a numerical value")
            voltage = input("Please input the measured Transducer Voltage")
        voltage = float(voltage)

        # verify inputs before loading into database
        print(f"You inputed: test id: {test_id}, actual pressure: {actual}, and transducer voltage: {voltage}.")
        decision = input("Do you want to input this into the database? (y/n)")

        if decision.lower() in ["y","yes"]: # load into database
            new_readings = {"test_id": test_id, "actual": actual, "transducer": voltage}
            self.sensor_data = pd.concat([self.sensor_data, pd.DataFrame([new_readings])], ignore_index=True)
            self.sensor_data.to_csv("LinearModelData.csv")
            print("Entries entered into the database.\n")
        else: # abort
            print("Entries were not entered into the database.\n")

    def train (self):
        #splitting data
        X = self.sensor_data[["transducer"]]
        y = self.sensor_data["actual"]

        self.model.fit(X,y) # no use excluding any data for test. Note evaluating model anyway

    def predict (self):
        # get voltage from user and format
        voltage = input("\nPlease input a voltage to predict a value")
        while not voltage.replace(".", "").isnumeric():
            print("Please enter a integer value")
            voltage = input("Please input a voltage to predict a value")
        voltage = float(voltage)
        volt_pred = pd.DataFrame({"transducer": [voltage]})

        # predict new pressure value
        pressure = self.model.predict(volt_pred)[0]
        print(f"The predicted pressure is {round(pressure, 2)} PSIG\n")

    def retrain (self):
        print("Retraining model with updated parameters...")
        self.train()
        print("Done! \n")
        
    def interface(self):
        command = None
        commands = ["exit", "retrain", "update", "predict","load", "reload"]
        # command_destinations contains all of our possible commands and corresponding functions
        command_destinations = {
            "exit": None,
            "retrain": self.retrain,
            "update": self.append_dataset,
            "predict": self.predict,
            "load": lambda: self.load_dataset(self.database_path),
            "reload": lambda: self.load_dataset(self.original_data_path)
            }

        print("This is your Pressure Sensor Interface!\n")

        while command != "exit":
            command = input(f"Choose one of the following commands: {", ".join(commands)}: ")
            while command not in commands:
                command = input(f"Choose one of the following commands: {", ".join(commands)}: ")
            if command == "exit":
                break
            else:
                command_destinations[command]()

        print("All data saved. Terminating")