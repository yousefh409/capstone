from analyze_video import analyze_video
import glob
import pandas as pd

data_path = '../../DATA/'

def generate_points(video_inf):
    points = {a: video_inf["points"][a] for a in list(video_inf["points"].keys())[1:]}
    velocities = video_inf["velocities"]
    generated = []
    for key in list(points.keys())[1:]:
        to_add = {
            "x": points[key]["x"],
            "y": points[key]["y"],
            "t": key,
            "vY": velocities[key]["vY"],
            "vX": velocities[key]["vX"],
            "vYinitial": list(velocities.values())[0]["vY"],
            "vXinitial": list(velocities.values())[0]["vX"],
        }
        generated.append(to_add)
    return generated



def main():
    videos = glob.glob(data_path + "*.mp4")
    data = pd.DataFrame([], columns=["x", "y", "t", "vY", "vX", "vXinitial", "vYinitial"])
    for video in videos:
        video_inf = analyze_video(video)
        generated_points = generate_points(video_inf)
        temp = pd.DataFrame(generated_points)
        data = data.append(temp)
    print(data)
    data.to_csv('data_points.csv', index=False)



if __name__ == "__main__":
    main()
