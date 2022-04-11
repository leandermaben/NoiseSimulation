import os
import json
import argparse

def execute(command):
    print(f'Executing {command}')
    exit_status = os.system(command)
    if exit_status > 0:
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Run Experiments')
    parser.add_argument('--experiment_name', dest='exp_name', type=str, default='sample_train.json', help='Name of JSON file with experiment parameters in the experiments folder.')

    args = parser.parse_args()

    with open(f'experiments/{args.exp_name}','r') as f:
        parameters = json.load(f)

    model_args = ''
    for key, value in parameters['model_args']:
        model_args+= f'--{key} {value} '

    if parameters['mode'] == 'train':
        os.chdir('src')
        execute(f'python train.py {model_args}')
        os.chdir('..')
    elif parameters['mode'] == 'test':
        os.chdir('src')
        execute(f'python test.py {model_args}')
        os.chdir('..')
    

