  textImage = ti.imgDisplay(list_text)  # Assuming this function works as expected
            for i in range(len(textImage)):
                myimage = img.imread(textImage[i])
                self.widget.canvas.axes.clear()
                self.widget.canvas.axes.imshow(myimage, cmap='gray')
                self.widget.canvas.draw()
                self.lineEdit_2.setText(str(list_text[i]))
                time.sleep(10)  # Wait for 10 seconds before displaying the next image