import numpy as np
import subprocess

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')
correct = np.mean(data_input,axis=1)

subprocess.run(["python", "sagital_brain.py"])

test = np.loadtxt("brain_average.csv",  delimiter=',')
#assert test == correct, 'Error test failed'
np.testing.assert_array_equal(correct,test)


