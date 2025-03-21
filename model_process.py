from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1


class Model():
    def select_model(self, language_type):
        if language_type == "en-tr":
            self.model_name = "Helsinki-NLP/opus-tatoeba-en-tr"
        else:
            self.model_name = f"Helsinki-NLP/opus-mt-{language_type}"
        self.translator = pipeline("translation", model=self.model_name, device=device)

    def use_model(self):
        return self.translator
