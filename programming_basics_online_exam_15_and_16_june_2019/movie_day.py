# Задача 2. Снимачен ден

# Снимачният ден започва с подготовка на терен, което е 15 процента от времето за снимки! Филмът има определен брой сцени,
# които се заснемат за определено време.
import math

time_for_photos = int(input())
number_of_scenes = int(input())
scene_duration = int(input())
total_need_time = number_of_scenes * scene_duration
movie_time = time_for_photos * 0.85
diff = abs(total_need_time - movie_time)

if movie_time >= total_need_time:
    print(f"You managed to finish the movie on time! You have {math.ceil(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {math.ceil(diff)} minutes.")






# Останалото време да се закръгли до най-близкото цяло число.
