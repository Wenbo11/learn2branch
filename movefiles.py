import os 
  
# importing shutil module  
import shutil 
  
shutil.rmtree('/Users/etashguha/Documents/learn2branch/data/instances/setcover/transfer_500r_1000c_0.05d')
os.mkdir('/Users/etashguha/Documents/learn2branch/data/instances/setcover/transfer_500r_1000c_0.05d')		
for i in range(100):
	source = f'/Users/etashguha/Documents/RL_branching/data/instances/setcover/train_200r_400c_0.1d_1mc_0se/instance_{i + 1}/instance_{i + 1}.lp'
	destination = f'/Users/etashguha/Documents/learn2branch/data/instances/setcover/transfer_500r_1000c_0.05d/instance_{i + 1}.lp'
	dest = shutil.copyfile(source, destination) 
