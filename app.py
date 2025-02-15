import assemblyai as aai


aai.settings.api_key = "dfa993e04c854aaea396a65bc05e7b80"

def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session opened with ID:", session_opened.session_id)


def on_error(error: aai.RealtimeError):
    print("Error:", error)


def on_close():
    print("Session closed")

def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        # Add new line after final transcript.
        print(transcript.text, end="\r\n")
    
        
transcriber = aai.RealtimeTranscriber(
    sample_rate=16_000,
    on_data=on_data,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close,
)

transcriber.connect()

microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)

transcriber.stream(microphone_stream)
