import seaborn as sns
import logging

def process_titanic_ds(output_path: str):    
    data = sns.load_dataset("titanic")
    logging.debug("Loaded dataset")

    survived = data.groupby("pclass")["survived"].mean()
    logging.debug("Aggregated data to get distribution of survivers by pclass")

    logging.debug("writing data to show_report.xlsx")
    survived.to_excel(output_path)


def process_w_error():
    raise ValueError("Some error occured during processing.")
