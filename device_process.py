import sounddevice as sd
import speech_recognition as sr

recognizer = sr.Recognizer()


class Device():
    def select_device(self, device_type):
        self.device_type = device_type

    def device_use_model(self, model):
        self.device_model = model

    def audio_language(self, lang_model_from):
        lang_data = {"tr": "tr-TR", "en": "en-EN", "es": "es-ES", "fr": "fr-FR"}
        self.lang_model = lang_data[lang_model_from]

    def get_device_list(self):
        devices = sd.query_devices()
        hostapis = sd.query_hostapis()
        index_list = [i["default_input_device"] for i in hostapis]
        device_list = [[i["name"] + " ...", i["index"]] for i in devices if i["index"] in index_list]
        return device_list

    def connect_device(self, index):
        try:
            with sr.Microphone(device_index=index) as source:
                recognizer.pause_threshold = 1.1
                recognizer.adjust_for_ambient_noise(source)
            self.listening = recognizer.listen_in_background(source, self.microphone)
        except Exception as e:
            print(e)

    def stop_connect(self):
        self.listening()

    def microphone(self, recognizer, recorded_audio):
        try:
            text = recognizer.recognize_google(recorded_audio, language=self.lang_model)
            decoded_text = self.translate(text)
            print("-" * 10)
            print("[TEXT]: {}".format(text))
            print("[TRANSLATED TEXT]: {}".format(decoded_text))
            print("-" * 10, end="\n\n")
        except Exception as e:
            print(str(e))

    def translate(self, text):
        translated_sentence = self.device_model(text)[0]["translation_text"]
        return translated_sentence
