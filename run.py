from paths import path_2_a, path_2_b, path_3_a, path_3_b, path_3_c, path_3_d, path_4_a, path_4_b
from utils import create_character_name
from story import start_story, finish_story


print("-" * 50)
print(" A messengers journey")
print("-" * 50)
print(" Instructions")
print("-" * 50)
create_character_name()
print("-" * 50)


start_story()
path_2_a()
path_2_b()
path_3_a()
path_3_b()
path_3_c()
path_3_d()
path_4_a()
path_4_b()
finish_story()
