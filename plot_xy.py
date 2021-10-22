import pandas as pd, sys, os
from plotnine import *

input_folder  = 'input/robot_recordings/'
output_folder = 'images/robot_experiment/'
stamps = ['1634838491.5258856']
sequences = ['fss','sfs','kkk']
trials_per_sequence = 2


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = [f'results_{s}_{q}_{i}.csv' for s in stamps for q in sequences for i in range(trials_per_sequence)]



for f in files:
	results = pd.read_csv(input_folder + f)

	plot = ggplot(results , aes('x', 'y')) + geom_point() + labs(x='x', y='y') + xlim(-1,1) +ylim(-1,1)

	ggsave(plot,filename=f'{output_folder}{f[0:-4]}.png')
