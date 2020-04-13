import os
import random
import time

from PIL import Image

from motya.motya import Motya
from motya.template import Template, Frame


if __name__ == "__main__":
    seed = time.time()
    print(f"Seed: {seed}")
    random.seed(seed)

    main_template = Template(
        image=Image.open("template.jpg"),
        width=574,
        height=522,
        frame=Frame(x_start=75, y_start=45, x_end=499, y_end=373),
        padding=10,
    )

    file_list = []
    for dirpath, dirnames, filenames in os.walk("images/"):
        for filename in [f for f in filenames if f.endswith(("png", "jpg", "jpeg"))]:
            file_list.append(Image.open(os.path.join("images/", filename)))

    motya = Motya(
        template=main_template,
        phrases=list(open("phrases.txt", encoding="utf-8").readlines()),
        images=file_list,
    )

    output = motya.generate()
    output.save("result.png")
    output.show()
