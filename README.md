# :wrench: Run Configurator 

This Python script gives you the possibility to have mutlitple run configurations. 
It's creating a config.json with the needed information. The script is looking for virtual environements in the folder. 


<br>

## :white_check_mark: Setup

1. Copy <b>RunConfigurator.py</b> file in the directory
2. Initialize script
```ps
python RunConfigurator.py -init
```
3. Add first configuration
```ps
python RunConfigurator.py -add
```
```ps
Add configuration: 
Name: 
Script Path (Enter absolute path): 
Script parameters (default: []): 
```
4. Run configuration
```ps
python RunConfigurator.py -NameOfConfiguration
```

