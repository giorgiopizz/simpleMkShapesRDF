from mkShapesRDF.processor.framework.module import Module
import sys


class GenericFormulaAdder(Module):
    def __init__(
        self, pathToConfigFile
    ):  # ='RPLME_FW/processor/data/formulasToAdd_Data.py'
        super().__init__("GenericFormulaAdder")
        self.pathToConfigFile = pathToConfigFile

    def runModule(self, df, values):
        print("Path to formulas: {}".format(self.pathToConfigFile))
        with open(self.pathToConfigFile) as file:
            handle = file.read()

        locs = {"df": df, "formulas": {}}
        exec(handle, {}, locs)
        formulas = locs["formulas"]
        setattr(self, "formulas", formulas)

        if len(list(self.formulas.keys())) == 0:
            print("No formulas found in {self.pathToConfigFile}")
            sys.exit(1)

        for key in self.formulas.keys():
            print("Key: {}, value: {}".format(key, self.formulas[key]))
            df = df.Define(key, self.formulas[key])

        return df
