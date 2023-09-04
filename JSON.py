import random

def generate_json(audio_distance, visual_distance, visual_vertical_rotation, visual_horizontal_interval, num_audio_sources):
    data = {
        "AudioOrigins": [],
        "VisualSources": [],
    }

    # Generate a list of possible horizontal rotations for audio sources.
    # Each rotation is a multiple of the visual_horizontal_interval.
    possible_horizontal_rots = list(range(0, 360, visual_horizontal_interval))

    # Randomly select horizontal and vertical rotations for the audio sources from the list of possible rotations.
    audio_horizontal_rots = random.choices(possible_horizontal_rots, k=num_audio_sources)
    audio_vertical_rots = random.choices(visual_vertical_rotation, k=num_audio_sources)

    for i in range(len(audio_horizontal_rots)):
        audio_origin_low = {
            "distance": audio_distance,
            "horizontalRotation": audio_horizontal_rots[i],
            "verticalRotation": -audio_vertical_rots[i],
            "frequency": 500,  # Lower frequency
            "name": f"audio-low-{audio_horizontal_rots[i]:02d}-{audio_vertical_rots[i]:02d}",
        }
        audio_origin_high = {
            "distance": audio_distance,
            "horizontalRotation": audio_horizontal_rots[i],
            "verticalRotation": -audio_vertical_rots[i],
            "frequency": 2500,  # Higher frequency
            "name": f"audio-high-{audio_horizontal_rots[i]:02d}-{audio_vertical_rots[i]:02d}",
        }
        data["AudioOrigins"].append(audio_origin_low)
        data["AudioOrigins"].append(audio_origin_high)


    for horizontal_rot in range(0, 360, visual_horizontal_interval):
        for vertical_rot in visual_vertical_rotation:
            visual_source = {
                "distance": visual_distance,
                "horizontalRotation": horizontal_rot,
                "verticalRotation": -vertical_rot,
                "name": f"visual-{horizontal_rot:02d}-{vertical_rot:02d}",
            }
            data["VisualSources"].append(visual_source)

    return data

