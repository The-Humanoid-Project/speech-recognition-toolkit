import speech_recognition as sr

r=sr.Recognizer()

class LISTENER():
    def listen(self,cond):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                if(cond):
                    MyText,confidence = r.recognize_google(audio,with_confidence=cond)
                    print(MyText,confidence)
                else:
                    MyText=r.recognize_google(audio)
                    print(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            self.msg.set("Message not Received, Speak Clearly")
            self.listen()

if __name__=="__main__":
    print("program started")
    sample=LISTENER()
    with_confindence=True
    sample.listen(with_confindence)