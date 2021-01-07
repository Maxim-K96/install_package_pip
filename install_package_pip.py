#!/usr/bin/env python3.8
#-*- encoding:utf8 -*-
# install_package_pip_auto позволяет создавать несколько потоков загрузки модулей Python 3x
# language doc: ru

__version__ = 1.0
__autor__ = 'Kolokoltsev Maxim'
__email__ = 'Kolokolcev20@mail.ru'

try:
  import sys
  import os
  from multiprocessing.dummy import Pool as TreadPool
except:
  raise ImportError

def install_pip(package):
  """Функция установки пакетов с помощью pip"""
  print('\n',' '*10,'='*10, ' install %s ' % package, '='*10, '\n')
  os.system('pip3 install {package}'.format(package=package))
# os.system('pypy3 -m pip install {package}'.format(package=package))

  print('\n', ' '*10, '*'*10, ' The end ', '*'*10, '\n')
  
def main():
  """Главная функция"""
  try: 
    tread = ''.join(sys.argv[1])
    packages = sys.argv[2:]
    if tread.isdecimal():
      pass
    else:
      description = """
Пожалуйста введите количество потоков в диапазоне от 1 до 8\n\n\tФормат записи:\ninstall_package_pip_auto.py treads -> int [packages] -> str\n\nВведите количество потоков: """
      tread = input(description)
      packages = sys.argv[1:]
  except IndexError:
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
        print('Модуль {package} является частью стандартного набора Python'.format(package=package))
    except(ImportError):
      install_package.append(package)

  pool = TreadPool(int(tread))
  pool.map(install_pip, install_package)
  pool.close()


if __name__=="__main__":
  main()
