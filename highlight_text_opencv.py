import cv2

TIME_CONTROL = 20
FONT = cv2.FONT_HERSHEY_SIMPLEX
T_COLOR = (255,255,255)                                 # text color: WHITE
# highlight
X_THICKNESS = 5
Y_THICKNESS = 15
H_COLOR = (0,0,0)                                       # highlight color: BLACK

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)            # This code works for real-time
capHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)      # recognition, but you can change it
capWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)        # for static images

i, length_control = 0, 0
words = ['']
sentences = ['A', 'B', ' ','123', ' ', 'TEST']          # just for tests.

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)

    sentence = ''.join(words)                           # list -> string
    if i % TIME_CONTROL == 0:
        # words.append(letter)                          # if you already have the letter
        if length_control < len(sentences):             # getting words from sentences test list
            words.append(sentences[length_control])
            length_control += 1

    # generate the sentence & highlights
    text_size = cv2.getTextSize(sentence, FONT, 1, 1)[0]
    coord_text_x = int((frame.shape[1] - text_size[0]) / 2)
    coord_text_y = int(((frame.shape[0] + text_size[1]) / 2) + (capHeight / 2.5))
    # `+ (capHeight / 2.5)` control y-axis. without that, the coord_text_y will represent the frame middle

    # highlight
    cv2.rectangle(
        frame,
        (coord_text_x + text_size[0] + X_THICKNESS, coord_text_y - text_size[1] - Y_THICKNESS),
        (coord_text_x - X_THICKNESS, coord_text_y + Y_THICKNESS),
        H_COLOR, -1                                     # rectangle thickness must be -1 to fill the shape
    )
    # text
    cv2.putText(frame, sentence, (coord_text_x, coord_text_y), FONT, 1, T_COLOR, 1)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == 27:                            # ESC
        break

    i += 1

capture.release()