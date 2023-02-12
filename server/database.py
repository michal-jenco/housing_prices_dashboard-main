from typing import Dict, Iterator, List, Union

from tinydb import TinyDB


class LocalDatabase:
    def __init__(self) -> None:
        self._db = TinyDB('server/db_file/db.json')
        self._table = self._db.table("Predictions")

        self._no_prediction_text = "Not predicted yet"
        self._unsuccessful_prediction_text = "Prediction unsuccessful, perhaps you didn't enter all the required parameters?"
        self._last_predicted_price = self._no_prediction_text

    def insert(self, data: Dict) -> None:
        self._table.insert(data)
        self._last_predicted_price = list(data.values())[-1]

    def get_last_predicted_price(self) -> Union[str, float]:
        return self._last_predicted_price

    def get_all_values(self) -> Iterator[List]:
        full_contents = self._table.all()
        all_values = []

        for prediction in full_contents:
            all_values.append(list(prediction.values()))
        return reversed(all_values)

    def unsuccessful_prediction(self) -> None:
        self._last_predicted_price = self._unsuccessful_prediction_text

    def reset_last(self) -> None:
        self._last_predicted_price = self._no_prediction_text
