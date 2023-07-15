import os

from Utils.general import load_yaml_file
from EDA.analysis_processing import load_data, explore_analyse


if __name__ == "__main__":
    params = load_yaml_file("../Data/params.yaml")
    pths = params["paths"]

    data_heart = load_data("../%s" % pths["fheart"])

    explore_analyse(data_heart, params)

    breakpoint()
