from textual.app import App
from textual.containers import Vertical
from textual.reactive import Reactive
from textual.widgets import Footer, Input, Static
from datetime import datetime

# class MessageFeed(ScrollView):
#     """A scrollable widget to display chat messages."""

#     def __init__(self):
#         super().__init__()
#         self.messages = Vertical()
#         self.set_content(self.messages)

#     def add_message(self, sender: str, text: str):
#         """Add a message to the feed."""
#         timestamp = datetime.now().strftime('%H:%M:%S')
#         message = Static(f"[{timestamp}] {sender}: {text}")
#         self.messages.mount(message)
#         self.scroll_end(animate=False)

class ChatApp(App):
    """A simple chat application using Textual."""

    CSS_PATH = "chat.css"
    message_input: Reactive[str] = Reactive("")

    def compose(self):
        """Compose the layout of the chat app."""
        # self.message_feed = MessageFeed()
        self.input_box = Input(placeholder="Type your message...", id="input")
        self.footer = Footer()
        # yield self.message_feed
        yield self.input_box
        yield self.footer

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle the input submission to send a message."""
        if event.value.strip():
            # self.message_feed.add_message("You", event.value.strip())
            event.input.value = ""  # Clear input after sending

    def on_key(self, event):
        """Handle key events for focus and usability."""
        if event.key == "escape":
            self.input_box.focus()

if __name__ == "__main__":
    ChatApp.run()

