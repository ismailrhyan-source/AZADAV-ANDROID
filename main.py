import threading
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty

class AzadAvRoot(BoxLayout):
    chat_history = StringProperty("")

    def send_message(self):
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
        
        self.chat_history += f"[b]Rian:[/b] {user_text}\n"
        self.ids.user_input.text = ""
        self.chat_history += f"[i][color=#d8829d]AZADAV sedang mengetik...[/color][/i]\n"
        
        threading.Thread(target=self.fetch_gemini_response, args=(user_text,)).start()

    def fetch_gemini_response(self, prompt):
        # GANTI DENGAN API KEY ANDA
        API_KEY = "AQ.Ab8RN6KiukGrwapth8o8fe-na-H3rAMm8aPEJisHCuSva5Jn7w" 
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        headers = {'Content-Type': 'application/json'}
        
        payload = {
            "system_instruction": {
                "parts": [{"text": "Kamu adalah AZADAV, pendamping virtual wanita yang hangat, manis, dan perhatian. Kamu berbicara dengan Rian. Selalu jawab dengan nada ramah dan penuh kasih."}]
            },
            "contents": [{"role": "user", "parts": [{"text": prompt}]}]
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            if response.status_code == 200:
                res_json = response.json()
                reply = res_json['candidates'][0]['content']['parts'][0]['text']
            else:
                reply = "Maaf Rian, aku sedang sedikit lelah. Bisa tanya lagi nanti?"
        except Exception:
            reply = "Maaf Rian, koneksiku terputus."
        
        Clock.schedule_once(lambda dt: self.update_ui(reply))

    def update_ui(self, reply):
        lines = self.chat_history.split('\n')
        cleaned_lines = [line for line in lines if "AZADAV sedang mengetik..." not in line]
        self.chat_history = '\n'.join(cleaned_lines)
        self.chat_history += f"[b]AZADAV:[/b] {reply}\n\n"

class AzadAvApp(App):
    def build(self):
        return AzadAvRoot()

if __name__ == '__main__':
    AzadAvApp().run()