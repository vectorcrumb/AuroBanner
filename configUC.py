import simplejson as json


def main():
    data = {}

    data['nrc_code'] = []
    carr = input("Ingresa el codigo de tu carrera. El codigo por defecto es 040013-Ingenieria Civil. Apreta ENTER para seleccionarlo.\n")
    data['code_car'] = carr if len(carr) >= 6 else "040013-Ingenieria Civil"
    data['username'] = input("Ingrese tu nombre de usuario UC:\n")
    data['password'] = input("Ingresa tu clave para tu usuario UC:\n")
    # TODO Sanitize semester input
    data['semestre'] = input("Ingresa el semestre academico que desees registrar. El formato debe ser 'YYYY-1' o 'YYYY-2', "
                             "donde '-1' o '-2' es el numero del semestre:\n")

    print("A continuacion, deberas ingresar tus NRC uno por uno. Para terminar de ingresar codigos, ingresa el valor 0."
          "Procura mantener el orden adecuado al ingresar estos codigos, pues se ingresaran a la plataforma en el"
          "orden entregado.")

    while True:
        nrc = input("Ingresa 0 para salir o ingresa un codigo NRC: ")
        if nrc == '0':
            print("Has finalizado el ingreso de NRC.")
            break
        if len(nrc) != 5 and not any(c.isalpha() for c in nrc):
            print("El NRC tiene largo invalido. Intenta de nuevamente.")
            continue
        try:
            nrc_cod = int(nrc)
            if nrc_cod == 0:
                print("Has finalizado el ingreso de NRC.")
                break
            chk_nrc = input("El NRC ingresado es: {}. Ingresalo nuevamente para confirmar: ".format(nrc_cod))
            if chk_nrc != nrc:
                print("El NRC ingresado no coincide con el original. Intenta nuevamente.")
                continue
            data['nrc_code'].append(nrc_cod)
            print("El NRC fue ingresado con exito. Los NRC inscritos hasta ahora son:\n{}".
                  format(str(data['nrc_code']).strip('[]').replace(', ', '\n')))
        except ValueError:
            print("El NRC ingresado no es un numero valido. Intenta nuevamente.")

    # print(data)
    print("Ahora, se guardara tu configuracion en el archivo, config.json. Por favor revisa el archivo previo a usar"
          "el programa. En caso de encontrar algun error, simplemente corre este configurador de nuevo.")
    with open("config.json", 'w') as config_file:
        json.dump(data, config_file, sort_keys=True, indent=4*' ')

if __name__ == '__main__':
    main()
