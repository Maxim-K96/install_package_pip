#!/usr/bin/env python3.8
#-*- encoding:utf8 -*-
# install_package_pip_auto позволяет создавать несколько потоков загрузки модулей Python 3x
# language doc: ru
# Author: Kolokoltsev Maxim
# E-mail: Kolokolcev20@mail.ru
#
# version 1.1b

try:
  import sys
  import os
  from multiprocessing.dummy import Pool as TreadPool
  from loguru import logger
  from datetime import datetime
except:
  raise ImportError('ModuleNotFound')
#  logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='10KB', compression='zip')

@logger.catch
class Install_pip_packages(object):
  def __init__(self, tread:int, packages:dict):
    self._checking_argv(tread, packages)

  def _install_package(self, package):
    """Метод установки пакетов с помощью pip"""
    print('\n',' '*10,'='*10, ' install %s ' % package, '='*10, '\n')
    os.system('pip3 install {package}'.format(package=package))
  # os.system('pypy3 -m pip install {package}'.format(package=package))

    print('\n', ' '*10, '*'*10, ' The end ', '*'*10, '\n')
  
  def _checking_argv(self, tread_argv, packages):
    """Метод проверки аргументов"""
    try: 
      tread = ''.join(tread_argv)
      if tread.isdecimal():
        pass
      else:
        msg = """\nПожалуйста введите количество потоков в диапазоне от 1 до 8"""
        logger.info(msg)
        tread = input('\nВведите количество потоков: ')
    except IndexError:
#      logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
      raise ErrorNotData('Пожалуйста введите количество потоков и устанавливаемые пакеты')

    if packages == []:
      msg = """Вы забыли указать устанавливаемые пакеты\nПожайлуста, укажите модули, которые вы хотите установить"""
#    raise SyntaxError('ModuleNotIncluded') #Модуль не вписан
      logger.info(msg)
      packages.append(input('\nВведите название модулей, которые вы хотите установить: '))

    install_package = []
    for package in packages:
      try:
        try:
          exec('import %s' % package)
          logger.info('Модуль {package} установлен в вашей системе'.format(package=package))
        except SyntaxError:
#          logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
          logger.info('Модуль {package} является частью стандартного набора Python'.format(package=package))
      except(ImportError):
#        logger.add('./logfiles/install_package_pip_%s.log'%datetime.today().strftime('%d.%m.%Y-%H:%M:%S'), format='{time}{level}{message}', level='ERROR', rotation='300KB', compression='zip')
        install_package.append(package)

    self._tread_pool(tread, install_package)

  def _tread_pool(self, tread, install_package):
    """ Метод многопоточности"""
    pool = TreadPool(int(tread))
    pool.map(self._install_package, install_package)
    pool.close()


if __name__=="__main__":

  try:
    tread = sys.argv[1]
    packages = sys.argv[2:]
  except IndexError:
    msg = """\nПожалуйста введите количество потоков в диапазоне от 1 до 8"""
    logger.info(msg)
    tread = input('\nВведите количество потоков: ')
    packages = sys.argv[1:]

  if tread.isdecimal():
    pass
  else:
    msg = """\nПожалуйста введите количество потоков в диапазоне от 1 до 8\n\n\tФормат записи:\ninstall_package_pip.py treads:int [packages]:str"""
    logger.info(msg)
    tread = input('\nВведите количество потоков: ')
    packages = sys.argv[1:]

  if packages == []:
    msg = """\nВы забыли указать устанавливаемые пакеты\nПожайлуста, укажите модули, которые вы хотите установить"""
#   raise SyntaxError('ModuleNotIncluded') #Модуль не вписан
    logger.info(msg)
    package = (input('\nВведите название модулей, которые вы хотите установить: ').split(' '))
    packages = [pack for pack in package]

  installer = Install_pip_packages(tread, packages)

