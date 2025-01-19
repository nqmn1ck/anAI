import json
import numpy.random as random
import numpy as np

'''
Procedural random trait and memory selector to create a new unique llmperson.
Prompt an llm to decide what personal background fits the randomly selected motivations and important memories?
'''

male_physical_traits_path =   "src/ana/person/physical_traits_m.json"
female_physical_traits_path = "src/ana/person/physical_traits_f.json"
emotional_traits_path =       "src/ana/person/emotional_traits.json"
personality_traits_path =     "src/ana/person/personality_traits.json"
important_memories_path =     "src/ana/person/important_memories.json"
personal_motivations_path =   "src/ana/person/personal_motivations.json"
personal_backgrounds_path =   "src/ana/person/personal_backgrounds.json"

save_path = "data/llmperson-generated-profile.json"

save_file = open(save_path, "w")

# 1) RANODMLY SELECT PHYSICAL TRAITS.
# - We will separate the body into bodyparts, such as nose, face, eyes, ears. 
#   Each bodypart will then be defined by multiple features and possibly subfeatures.

f = open(female_physical_traits_path) # currently we will only use a female llmperson
physical_traits = json.load(f)
selection = {}
for bodypart, bodypart_dict in physical_traits.items():
  selection[bodypart] = {} # Dict to store body part component selections
  for bodypart_feature, bodypart_feature_options in bodypart_dict.items():
    # Case: there is a subfeature
    if isinstance(bodypart_feature_options, dict):
      for bodypart_subfeature, bodypart_subfeature_options in bodypart_feature_options.items():
        if bodypart_feature == "UniqueFeatures":
          # Select multiple component options
          num_selections = random.choice(np.arange(1, len(bodypart_subfeature_options) + 1))
          selection[bodypart][bodypart_feature] = random.choice(bodypart_subfeature_options, num_selections, replace=False).tolist()
        else:
          # Select only one component option
          selection[bodypart][bodypart_feature] = random.choice(bodypart_subfeature_options).tolist()

    # Case: no subfeature
    elif bodypart_feature == "UniqueFeatures":
      # Select multiple component options
      num_selections = random.choice(np.arange(1, len(bodypart_feature_options) + 1))
      selection[bodypart][bodypart_feature] = random.choice(bodypart_feature_options, num_selections, replace=False).tolist()
    else:
      # Select only one component option
      selection[bodypart][bodypart_feature] = random.choice(bodypart_feature_options).tolist()
selection = {"Physical Traits": selection}
save_file.write(json.dumps(selection, indent=2)) # Legible version
#json.dump(selection, save_file) # Character-efficient version

f.close()

# Select emotional traits
f = open(emotional_traits_path)
f.close()

# Select personality traits
f = open(personality_traits_path)
f.close()

# Important memories
f = open(emotional_traits_path)
f.close()

# Personal motivations
f = open(personal_motivations_path)
f.close()

# Personal background
f = open(personal_backgrounds_path)
f.close()

save_file.close()