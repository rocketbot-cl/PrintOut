# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import sys
import os
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'PrintOut' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from colorama import init as c_init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
c_init()

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Reviso que tipo de modulo es
"""
if module == "PrintOut":
    data = GetParams("data")
    decorator = GetParams("decorator")
    color_ = GetParams("color")
    pre_data = None
    c_ = None
    if decorator:
        try:
            color_ = color_.lower()
            print(colored(decorator * 20, color_))
            print(colored(data, color_))
            print(colored(decorator * 20, color_))
        except Exception as e:
            print(e)
    else:
        try:
            print(colored(data, color_))
        except:
            try:
                print(data)
            except Exception as e:
                print(e)
                raise Exception(e)