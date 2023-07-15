import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Utils.general import find_two_numbers


def load_data(fname: str):
    return pd.read_csv(fname)


def general_description(df: pd.DataFrame):
    print("\n--------- Head of the dataset ---------")
    hd = df.head()
    print(hd)
    print("\n--------- Stats description ---------")
    des = df.describe().T
    print(des)
    # print("--------- Information on columns ---------")
    # print(df.info())
    print("\n--------- Number of NaN values per column ---------")
    count_nan_values = df.isna().sum()
    print(count_nan_values)
    print("\n--------- Number of unique values per column ---------")
    count_unique_values = df.nunique()
    print(count_unique_values)


def visualization_plots(df: pd.DataFrame):
    print("\n--------- Plot histogram for each variable ---------")
    df.hist(figsize=(10, 6))
    plt.tight_layout()
    plt.show()

    print("\n--------- Plot a heatmap to visualize correlations between variables ---------")
    # Create a correlation matrix
    corr_matrix = df.corr()
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

    # print("\n--------- Box plots for each variable (sorted by output variable) ---------")
    # n = len(df) - 1
    # k1, k2 = find_two_numbers(n)
    # fig, axes = plt.subplots(k1, k2, figsize=(8, 6))
    # num_var = 0
    # for i in range(k1 - 1):
    #     for j in range(k2 - 1):
    #         axx = axes[i][j]
    #         var = df.columns[num_var]
    #         if num_var <= len(df.columns):
    #             sns.boxplot(data=df, x='output', y=df.columns[num_var], ax=axx)
    #             axx.set_title('Box Plot - %s' % var)
    #         num_var += 1
    # plt.suptitle('Box Plots - Variables Separated by Output')
    # plt.tight_layout()
    # plt.show()


def explore_analyse(df: pd.DataFrame, prm: dict):
    print("============= Exploring/Analysing Input DataFrame =============")

    # 1st steps
    general_description(df)

    # 2nd steps
    visualization_plots(df)

    print("\n--------- Separate continuous, categorical and target variables ---------")
    vars = prm["variables"]
    cat_cols = vars["cat_cols"]
    cont_cols = vars["cont_cols"]
    target_cols = vars["target_cols"]
    print("     > The categorical cols are: ", cat_cols)
    print("     > The continuous cols are: ", cont_cols)
    print("     > The target variable is:  ", target_cols)

    # print("\n--------- Plot pairwise bi-variate distributions ---------")
    # print("\n       > On categorical variables ---------")
    # plt.figure(figsize=(10, 8))
    # sns.pairplot(df[cat_cols + target_cols], hue="output")
    # plt.legend("output")
    # plt.show()
    # print("\n       > On continuous variables ---------")
    # plt.figure(figsize=(10, 8))
    # sns.pairplot(df[cont_cols + target_cols], hue="output")
    # plt.legend("output")
    # plt.show()