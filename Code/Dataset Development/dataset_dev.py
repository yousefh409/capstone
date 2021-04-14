from analyze_video import analyze_video
import glob
import pandas as pd

data_path = '../../DATA/'

def generate_points(video_inf):
    points = {a: video_inf["points"][a] for a in list(video_inf["points"].keys())[1:]}
    velocities = video_inf["velocities"]

    generated = []
    
    for i in range(len(list(points.keys())[:-1])):
        for key in list(points.keys())[i + 1:]:
            to_add = {
                "x": points[key]["x"] - points[list(points.keys())[i]]["x"],
                "y": points[key]["y"] - points[list(points.keys())[i]]["y"],
                "t": key - list(points.keys())[i],
                "vY": velocities[key]["vY"],
                "vX": velocities[key]["vX"],
                "vYinitial": list(velocities.values())[i]["vY"],
                "vXinitial": list(velocities.values())[i]["vX"],
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
