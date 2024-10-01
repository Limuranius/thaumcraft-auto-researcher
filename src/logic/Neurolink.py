from dataclasses import dataclass

from PIL import Image

from logic.onnx_inference import preprocess, predict, postprocess, class_names


@dataclass
class Prediction:
    x: float
    y: float
    width: float
    height: float
    predictionName: str
    confidence: float


class _NeurolinkClass:
    model: any
    inputModelName: str
    outputModelName: str
    isConnectionError: bool
    minConfidence: float = 0.6
    overlap: float = 0.3

    # Make it singleton
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_NeurolinkClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __init__(self):
        pass

    def predict(self, image: Image.Image):
        image = image.convert("RGB")
        preproc_image, returned_metadata = preprocess(image)
        predicted_arrays = predict(preproc_image)
        postprocessed = postprocess(predicted_arrays, returned_metadata)[0]

        result = list(map(lambda prediction: Prediction(
            prediction[0] + abs(prediction[0] - prediction[2]) / 2,
            prediction[1] + abs(prediction[1] - prediction[3]) / 2,
            abs(prediction[0] - prediction[2]),
            abs(prediction[1] - prediction[3]),
            class_names[int(prediction[6])],
            prediction[4],
        ), postprocessed))

        image = image.copy()

        from PIL import ImageDraw
        draw = ImageDraw.ImageDraw(image)
        for x, y, x1, y1, conf, conf, label in postprocessed:
            draw.rectangle([x, y, x1, y1])
            draw.text([x, y], str(class_names[int(label)]))
        image.show()

        return result


Neurolink = _NeurolinkClass()
