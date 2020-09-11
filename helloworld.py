# -*- coding: utf-8 -*-
# @Time: 2020/9/11 0:02
# @Author: Rollbear
# @Filename: helloworld.py

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier  # knn
from sklearn.externals import joblib  # model load / save


def main():
    # file io path
    input_path = "./resource/e1.xlsx"
    log_output_path = "./model/knn_log.txt"
    model_dump_path = "./model/knn.model"

    # params of classifier
    leaf_size = 0
    n_neighbors = 0

    # predicted labels
    y_labels = ["A", "B", "C", "D"]
    # x_frame = pd.DataFrame()

    # file io
    # todo::use component of pandas to read excel.
    data = pd.read_excel(input_path, sheet_name="企业信息")

    # knn model init
    knn_model = KNeighborsClassifier(leaf_size=leaf_size,
                                     n_neighbors=n_neighbors)
    # knn_model.fit()


def load_stock_info(df: pd.DataFrame):
    pass



if __name__ == '__main__':
    main()
