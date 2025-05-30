
from logging import getLogger
logger = getLogger(__name__)
from tool import log_init
output_dir = log_init() #他のツールをimportした際にloggerが使われると記録されないので早々に実行。

import sys,os,datetime,subprocess,shutil


def init(output_dir:str):
    if os.path.isdir('.git')==False:
        print('this project is not managed with git.')
    else:
        def exec_and_show(command:str):
            logger.info(command+'\n'+subprocess.run(command, shell=True, text=True, capture_output=True).stdout)
        logger.info('*****show git info start*****')
        exec_and_show('git status')
        exec_and_show('git rev-parse HEAD')
        exec_and_show('git --no-pager log -n 3')
        exec_and_show('git --no-pager diff -p')
        logger.info('*****show git info end*****')

    shutil.copytree('./code/', output_dir+'/code', copy_function=shutil.copy2)

def main():
    start_time = datetime.datetime.now()
    logger.info(f'program start. sys.args:{sys.argv}')
    init(output_dir)


    logger.debug('message as debug')
    logger.info('message as info')
    logger.warning('message as warning')
    logger.error('message as error')


    logger.info(f'program finished. elapsed:{datetime.datetime.now()-start_time}')

if __name__ == '__main__':
    main()
