import os,time,datetime
from logging import getLogger, config as logging_config_func
logger = getLogger('__main__').getChild(__name__)


def create_output_dir(output_dir:str=None) -> str:
    #output_dirが指定された場合、その名前で作る。
    if output_dir is not None:
        os.makedirs(output_dir, exist_ok=False)
        return output_dir

    #output_dirが指定されなかった場合、日時を含む名前で適当に作る。
    #すでにあるディレクトリ名で作ろうとした場合は別の名前に。
    while True:
        now = datetime.datetime.now()
        output_dir = f"output_dir_{now.strftime('%Y%m%d_%H%M%S')}_{now.microsecond:06d}"
        try:
            os.makedirs(output_dir, exist_ok=False)
            break
        except OSError as e:
            pass
        time.sleep(0)
    return output_dir

def logging_config(output_dir:str) -> None:
    log_conf = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s %(name)s:%(lineno)s %(funcName)s %(levelname)s] %(message)s'
            }
        },
        'handlers': {
            'consoleHandler': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'fileHandler': {
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'filename': f'{output_dir}/log.txt'
            }
        },
        'root': {
            'level': 'DEBUG', #DEBUG,INFO,WARNING,ERRORの順でログ出力対象が減る。
            'handlers': ['consoleHandler', 'fileHandler'],
        }
    }
    logging_config_func.dictConfig(log_conf)

def log_init() -> str:
    output_dir = create_output_dir()
    logging_config(output_dir)
    return output_dir



def myfunc2_in_tool():
    logger.debug('message as debug')
    logger.info('message as info')
    logger.warning('message as warning')
    logger.error('message as error')

