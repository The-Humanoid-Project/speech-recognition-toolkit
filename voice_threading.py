import threading
from voice_recognition import LISTENER
import tkinter as tk

thread_running = True

my_queue = []
my_lock = threading.Lock()

# Writing thread


def writer_thread(x):
    with my_lock:
        my_queue.append(x)

# Reading thread


def reader_thread():
    with my_lock:
        if len(my_queue) > 0:
            return " " + my_queue.pop(0)
        else:
            return ""


def recognise_voice():
    global speak_now
    global thread_running
    Voice = LISTENER()
    while thread_running:
        speak_now = True
        recognized_text = Voice.listen(False)
        writer_thread(recognized_text)
        speak_now = False


def display_vals():
    # GUI for Humanoid
    global speak_now
    global thread_running
    root = tk.Tk()
    root.title("Voice Threading Application")
    root.geometry("900x150")

    l = tk.Label(root, text="The Humanoid Project")
    l.config(font=("Courier", 22))
    l.pack()

    curr_l = tk.Label(root, text="You said the following things:")
    curr_l.config(font=("Courier", 12))
    curr_l.pack()

    curr_t = tk.Label(root, text="The transcript will appear here")
    curr_t.config(font=("Courier", 12))
    curr_t.pack()

    root.update()

    transcript = ""
    pre_transcript = ""

    while thread_running:
        transcript += reader_thread()

        if (pre_transcript != transcript):
            curr_t.destroy()
            curr_t = tk.Label(root, text=transcript)
            curr_t.config(font=("Courier", 12))
            curr_t.pack()
            root.update()
            pre_transcript = transcript


if __name__ == "__main__":
    thread_1 = threading.Thread(target=display_vals)
    thread_2 = threading.Thread(target=recognise_voice)

    # Start the threads
    thread_1.start()
    thread_2.start()

    try:
        # Keep the main thread running
        while True:
            pass
    except KeyboardInterrupt:
        # Terminate the threads when the user interrupts the program
        print("Program interrupted. Terminating threads...")
        thread_running = False
        thread_1.join()
        thread_2.join()
