import yaml
#######################################################
#This python script involving accessing testEnv content present in config.yaml file
#with open('config.yaml', 'r') as f:
yaml_file= open('config.yaml','r')
yaml_data= yaml.load(yaml_file)
global s;
global test_percent;
s='preProdEnv'
test_percent=yaml_data['Test_Servers'][s]
#######################################################
