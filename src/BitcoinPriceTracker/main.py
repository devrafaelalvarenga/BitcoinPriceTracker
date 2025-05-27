from .extract.extract import extract
from .transform.transform import transform
from .load.load import load


if __name__ == "__main__":

    raw_data = extract()
    updated_data = transform(raw_data=raw_data)
    load(updated_data=updated_data)
