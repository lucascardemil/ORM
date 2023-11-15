from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import imutils
import cv2
import os
from flet import *
# import shutil
# from PIL import Image, ImageTk

class Scanner(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def build(self):
    self.vertical_alignment = MainAxisAlignment.CENTER
    # upload_button = Ref[ElevatedButton]()
    upload_button_test = Ref[ElevatedButton]()
    # selected_files = Text()
    selected_files_test = Text()

    # def abrir_archivo_guardar(e: FilePickerResultEvent):
    #     upload_button.current.disabled = True if e.files is None else False
    #     selected_files.value = (
    #         ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    #     )
    #     selected_files.update()
    #     page.update()

    # imagen_guardar = FilePicker(on_result=abrir_archivo_guardar)
    
    def abrir_archivo_revisar(e: FilePickerResultEvent):
        upload_button_test.current.disabled = True if e.files is None else False
        selected_files_test.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files_test.update()
        self.update()

    imagen_revisar = FilePicker(on_result=abrir_archivo_revisar)
    
    def orm(e, name):
        ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
        
        image = cv2.imread(imagen_revisar.result.files[0].path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 75, 200)

        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        docCnt = None

        if len(cnts) > 0:
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                if len(approx) == 4:
                    docCnt = approx
                    break

        paper = four_point_transform(image, docCnt.reshape(4, 2))
        warped = four_point_transform(gray, docCnt.reshape(4, 2))
        thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        questionCnts = []

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                questionCnts.append(c)

        questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
        correct = 0

        for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
            cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
            bubbled = None

            for (j, c) in enumerate(cnts):
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 255, -1)
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                total = cv2.countNonZero(mask)

                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, j)

            color = (255, 0, 0)
            k = ANSWER_KEY[q]

            if k == bubbled[1]:
                color = (0, 255, 0)
                correct += 1

            cv2.drawContours(paper, [cnts[k]], -1, color, 3)

        score = (correct / 5.0) * 100
        print("[INFO] score: {:.2f}%".format(score))
        cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        resultado_escritura = cv2.imwrite(os.path.join("./reviewed/", f"{name}.jpg"), paper)

        if resultado_escritura:
            self.page.snack_bar = SnackBar(Text("Imagen guardada con éxito en la carpeta de destino.", color="white"), bgcolor="green")
            self.page.snack_bar.open = True
            self.page.update()
        else:
            self.page.snack_bar = SnackBar(Text("Error al guardar la imagen.", color="white"), bgcolor="red")
            self.page.snack_bar.open = True
            self.page.update()

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            self.page.update()
        else:
            name = txt_name.value
            orm(e, name)

    # def upload_files(e):
    #         destination_folder = "./examenes/"

    #         if imagen_guardar.result is not None and imagen_guardar.result.files is not None:
    #             for f in imagen_guardar.result.files:
    #                 shutil.copy(f.path, destination_folder)

    txt_name = TextField(label="Nombre Alumno")

    self.page.overlay.append(imagen_revisar)

    return Column(
        controls = [
            Container(
                theme=Theme(color_scheme=ColorScheme(primary=colors.YELLOW)),
                content = Column(
                    controls=[
                        # Row([
                        #         ElevatedButton("Seleccionar archivo", icon=icons.FOLDER_OPEN, on_click=lambda _: imagen_guardar.pick_files()),
                        #         selected_files,
                        # ]),
                        # ElevatedButton("Upload", ref=upload_button, icon=icons.UPLOAD, on_click=upload_files, disabled=True),
                        txt_name,
                        Row([
                            ElevatedButton("Seleccionar archivo", icon=icons.FOLDER_OPEN, on_click=lambda _: imagen_revisar.pick_files()),
                            selected_files_test,
                        ]),
                        ElevatedButton("Revisar", ref=upload_button_test, on_click=btn_click, disabled=True)
                    ]
                )
            )
        ]
    )