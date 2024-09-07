#abstracao 
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplemented('Implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Error!')
    lp.log_sucess('Ok')
    lf = LogFileMixin()
    lf.log_error('File error')
    lf.log_sucess('File sucess')