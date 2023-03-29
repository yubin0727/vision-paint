import numpy as np
import cv2 as cv
    
def mouse_event_handler(event, x, y, flags, param):
    # Change 'mouse_state' (given as 'param') according to the mouse 'event'
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
    elif event == cv.EVENT_MOUSEMOVE and param[0]:
        param[1] = (x, y)
        
def draw_circle(event, x, y, flags, param):
    global left_x, left_y
    if event == cv.EVENT_LBUTTONDOWN:
        left_x = x
        left_y = y
    elif event == cv.EVENT_LBUTTONUP:
        if brush_mode == 1:
            cv.line(canvas, (left_x, left_y), (x, y), palette[brush_color], brush_radius)
        elif brush_mode == 2:
            center_x = int((x+left_x) / 2)
            center_y = int((y+left_y) / 2)
            axes_x = int((x-left_x) / 2)
            axes_y = int((y-left_y) / 2)
            cv.ellipse(canvas, (center_x, center_y), (axes_x, axes_y), 0, 0, 360, palette[brush_color], brush_radius)
        elif brush_mode == 3:
            center_x = int((x+left_x) / 2)
            center_y = int((y+left_y) / 2)
            axes_x = int((x-left_x) / 2)
            axes_y = int((y-left_y) / 2)
            cv.ellipse(canvas, (center_x, center_y), (axes_x, axes_y), 0, 0, 360, palette[brush_color], -1)
        elif brush_mode == 4:
            cv.rectangle(canvas, (left_x, left_y), (x, y), palette[brush_color], brush_radius)
        elif brush_mode == 5:
            cv.rectangle(canvas, (left_x, left_y), (x, y), palette[brush_color], -1)  
            

def free_drawing(canvas_width=640, canvas_height=480, init_brush_radius=3):
    # Prepare a canvas and palette
    mode = ['Point', 'Line', 'Unfilled Ellipse', 'Filled Ellipse', 'Unfilled Rectangle', 'Filled Rectangle']

    # Initialize drawing states
    mouse_state = [False, (-1, -1)] # Note) [mouse_left_button_click, mouse_xy]
    global brush_color, brush_mode, brush_radius
    brush_color = 0
    brush_mode = 0  
    brush_radius = 3
    
    # Instantiate a window and register the mouse callback function
    cv.namedWindow('Free Drawing')
    cv.setMouseCallback('Free Drawing', mouse_event_handler, mouse_state)
        
    while True:
        if brush_mode == 0:
            mouse_left_button_click, mouse_xy = mouse_state
            if mouse_left_button_click:
               cv.circle(canvas, mouse_xy, brush_radius, palette[brush_color], -1)
        
        # Show the canvas
        canvas_copy = canvas.copy()
        radius_info = f'Brush Radius: {brush_radius}'
        mode_info = f'Brush Mode: {mode[brush_mode]}'
        cv.putText(canvas_copy, radius_info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (127, 127, 127), thickness=2)
        cv.putText(canvas_copy, radius_info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, palette[brush_color])
        cv.putText(canvas_copy, mode_info, (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.6, (127, 127, 127), thickness=2)
        cv.putText(canvas_copy, mode_info, (10, 50), cv.FONT_HERSHEY_DUPLEX, 0.6, palette[brush_color])
        cv.imshow('Free Drawing', canvas_copy)

        # Process the key event
        key = cv.waitKey(1)
        if key == 27: # ESC
            break
        elif key == ord('\t'):
            brush_color = (brush_color + 1) % len(palette)
        elif key == ord('+') or key == ord('='):
            brush_radius += 1
        elif key == ord('-') or key == ord('_'):
            brush_radius = max(brush_radius - 1, 1)
        elif key == ord(' '):
            brush_mode = (brush_mode + 1) % len(mode)
            if brush_mode != 0:
                cv.setMouseCallback('Free Drawing', draw_circle)    
            else:
                cv.setMouseCallback('Free Drawing', mouse_event_handler, mouse_state)
                
                

    cv.destroyAllWindows()

if __name__ == '__main__':

    canvas = np.full((640, 480, 3), 255, dtype=np.uint8)
    palette = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    free_drawing()
