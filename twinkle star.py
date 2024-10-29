import numpy as np
import sounddevice as sd

# Define musical parameters
SAMPLE_RATE = 44100
AMPLITUDE = 0.3
TEMPO = 120
BEAT_DURATION = 60 / TEMPO


# Define musical parameters
SAMPLE_RATE = 44100  # Samples per second
AMPLITUDE = 0.3  # Reduced amplitude to prevent clipping
TEMPO = 120  # Beats per minute
BEAT_DURATION = 60 / TEMPO  # Duration of one beat in seconds


def generate_tone(frequency, duration):
    """Generate a tone with a smooth envelope"""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = np.sin(2 * np.pi * frequency * t)

    # Shorter envelope for quicker transitions
    attack_time = 0.005  # 5ms attack
    release_time = 0.005  # 5ms release

    # Create envelope
    attack = np.linspace(0, 1, int(SAMPLE_RATE * attack_time))
    sustain = np.ones(int(SAMPLE_RATE * (duration - attack_time - release_time)))
    release = np.linspace(1, 0, int(SAMPLE_RATE * release_time))
    envelope = np.concatenate([attack, sustain, release])

    # Ensure envelope and tone have the same length
    if len(envelope) > len(tone):
        envelope = envelope[:len(tone)]
    elif len(envelope) < len(tone):
        envelope = np.pad(envelope, (0, len(tone) - len(envelope)), 'edge')

    return (tone * envelope * AMPLITUDE).astype(np.float32)


def play_sequence(sequence):
    """Play a sequence of tones continuously"""
    # Concatenate all tones into one continuous array
    combined_tones = (np.concatenate
                      ([generate_tone(freq, dur) for freq, dur in sequence]))
    try:
        sd.play(combined_tones, SAMPLE_RATE, blocking=True)
    except Exception as e:
        print(f"Error playing sequence: {e}")
        return False
    return True


# Define musical notes frequencies
NOTES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88
}


def play_twinkle_star():
    """Play Twinkle Twinkle Little Star"""
    # Convert note names to frequencies with durations
    # Each number represents beats (1 = quarter note, 0.5 = eighth note, etc.)
    melody = [
        # Twinkle, twinkle, little star
        ('C4', BEAT_DURATION), ('C4', BEAT_DURATION),
        ('G4', BEAT_DURATION), ('G4', BEAT_DURATION),
        ('A4', BEAT_DURATION), ('A4', BEAT_DURATION),
        ('G4', BEAT_DURATION * 2),

        # How I wonder what you are
        ('F4', BEAT_DURATION), ('F4', BEAT_DURATION),
        ('E4', BEAT_DURATION), ('E4', BEAT_DURATION),
        ('D4', BEAT_DURATION), ('D4', BEAT_DURATION),
        ('C4', BEAT_DURATION * 2),

        # Up above the world so high
        ('G4', BEAT_DURATION), ('G4', BEAT_DURATION),
        ('F4', BEAT_DURATION), ('F4', BEAT_DURATION),
        ('E4', BEAT_DURATION), ('E4', BEAT_DURATION),
        ('D4', BEAT_DURATION * 2),

        # Like a diamond in the sky
        ('G4', BEAT_DURATION), ('G4', BEAT_DURATION),
        ('F4', BEAT_DURATION), ('F4', BEAT_DURATION),
        ('E4', BEAT_DURATION), ('E4', BEAT_DURATION),
        ('D4', BEAT_DURATION * 2),

        # Twinkle, twinkle, little star
        ('C4', BEAT_DURATION), ('C4', BEAT_DURATION),
        ('G4', BEAT_DURATION), ('G4', BEAT_DURATION),
        ('A4', BEAT_DURATION), ('A4', BEAT_DURATION),
        ('G4', BEAT_DURATION * 2),

        # How I wonder what you are
        ('F4', BEAT_DURATION), ('F4', BEAT_DURATION),
        ('E4', BEAT_DURATION), ('E4', BEAT_DURATION),
        ('D4', BEAT_DURATION), ('D4', BEAT_DURATION),
        ('C4', BEAT_DURATION * 2)
    ]

    print("Playing Twinkle Twinkle Little Star...")
    print(f"Tempo: {TEMPO} BPM")

    try:
        # Convert notes to frequency-duration pairs
        frequency_sequence = [(NOTES[note], duration) for note, duration in melody]
        play_sequence(frequency_sequence)

    except KeyboardInterrupt:
        print("\nMusic stopped by user")
        sd.stop()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        try:
            sd.stop()
        except:
            pass

    print("Music finished playing")


if __name__ == "__main__":
    print("Testing sound system...")

    try:
        sd.query_devices()
        print("Sound system initialized successfully")
    except Exception as e:
        print(f"Error initializing sound system: {e}")
        exit(1)

    print("\nMake sure you have the required library installed:")
    print("pip install numpy sounddevice")
    print("\nStarting the music program...\n")

    play_twinkle_star()
