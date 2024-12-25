# program checks sound devices plugged into the computer
import sounddevice as sd

def list_audio_devices():
    print("Available audio devices:")
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"{i}: {device['name']} (Channels: {device['max_input_channels']} in / {device['max_output_channels']} out)")

def check_speaker_output():
    print("\nTesting speaker output... (Ensure volume is turned up)")
    try:
        fs = 44100  # Sample rate
        duration = 2  # seconds
        frequency = 440  # A4 note
        
        # Generate a simple sine wave
        t = (sd.time() + np.arange(fs * duration)) / fs
        sound_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
        
        sd.play(sound_wave)
        sd.wait()
        print("Did you hear the sound? If yes, speakers are working!")
    except Exception as e:
        print("Error testing speaker output:", e)

# Execute functions
list_audio_devices()
check_speaker_output()

