import json

from Scripts.Token import dataPath

class Weight:
    def __init__(self, weight, value, answer, tags, need_question):
        self.weight = weight
        self.value = value
        self.answer = answer
        self.tags = tags
        self.need_question = need_question


class Blank:
    id = int()
    chat_info = str()

class DataWeight:
    def __init__(self):
        self.weight_words = []

    def get_weight(self):
        return self.weight_words

    def data_decoder(self, obj):
        return Weight(obj['weight'], obj['value'], obj['answer'], obj['tags'], obj['need_question'])

    def load_from_json(self):
        with open(dataPath, "r") as openfile:
            json_object = json.load(openfile, object_hook=self.data_decoder)
        return json_object


    # json load
    def load_to_json(self, data):
        json_object = json.dumps([obj.__dict__ for obj in data], indent=2, ensure_ascii=False)

        with open(dataPath, "w", encoding="utf-8") as outfile:
            outfile.write(json_object)







