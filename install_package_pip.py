#!/usr/bin/env python3.8
#-*- encoding:utf8 -*-
# install_package_pip_auto позволяет создавать несколько потоков загрузки модулей Python 3x
# language doc: ru

try:
  import sys
  import os
  from multiprocessing.dummy import Pool as TreadPool
  from loguru import logger
  from datetime import datetime
except:
  raise ImportError
  logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')

@logger.catch
class Install_pip_packages(object):
  def __init__(self, tread=sys.argv[1], packages=sys.argv[2:]):
    self.checking_argv(tread, packages)

  def info(self):
    __version__ = '1.0'
    __autor__ = 'Kolokoltsev Maxim'
    __email__ = 'Kolokolcev20@mail.ru'

  def install_package(self, package):
    """Метод установки пакетов с помощью pip"""
    print('\n',' '*10,'='*10, ' install %s ' % package, '='*10, '\n')
    os.system('pip3 install {package}'.format(package=package))
  # os.system('pypy3 -m pip install {package}'.format(package=package))

    print('\n', ' '*10, '*'*10, ' The end ', '*'*10, '\n')
  
  def checking_argv(self, tread_argv, packages):
    try: 
      tread = ''.join(tread_argv)
      if tread.isdecimal():
        pass
      else:
        description = """
  Пожалуйста введите количество потоков в диапазоне от 1 до 8\n\n\tФормат записи:\ninstall_package_pip_auto.py treads -> int [packages] -> str\n\nВведите количество потоков: """
        tread = input(description)
        packages = sys.argv[1:]
    except IndexError:
      logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
      description = """
  Формат записи:\ninstall_package_pip_auto.py treads -> int [packages] -> str\nПожалуйста введите количество потоков и устанавливаемые пакеты"""
      print(description)
      sys.exit()

    if packages == []:
      description = """
  Вы забыли указать устанавливаемые пакеты\nПожайлуста, укажите модули, которые вы хотите установить\nФормат записи:\n\tinstall_package_pip_auto.py treads -> int [packages] -> str\nПример:\n\tinstall_package_pip_auto.py 2 numpy spyder Pandas md5\n\nВведите название модулей, которые вы хотите установить: """
  #    raise SyntaxError('ModuleNotIncluded') #Модуль не вписан
      packages.append(input(description))

    install_package = []
    for package in packages:
      try:
        try:
          exec('import %s' % package)
          print('Модуль {package} установлен в вашей системе'.format(package=package))
        except SyntaxError:
          logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
          print('Модуль {package} является частью стандартного набора Python'.format(package=package))
      except(ImportError):
        logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
        install_package.append(package)

    self.tread_pool(tread, install_package)

  def tread_pool(self, tread, install_package):
    pool = TreadPool(int(tread))
    pool.map(self.install_package, install_package)
    pool.close()


if __name__=="__main__":
  installer = Install_pip_packages()
