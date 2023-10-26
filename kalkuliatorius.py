while True:
    print("Pasirinkite norimą atlikti veiksmą:\n"
          "1) Sudėtis\n"
          "2) Atimtis\n"
          "3) Daugyba\n"
          "4) Dalyba\n"
          "5) Skaičių seka\n"
          "0) Išeiti")

    veiksmas = input(">>> ")
    if veiksmas == '0':
        print('Programos pabaiga')
        break

    if veiksmas not in ['0', '1', '2', '3', '4', '5']:
        print("Tokio pasirinkimo nėra\n")
        continue

    pirmas_sk = int(input("Įveskite pirmą skaičių: "))
    antras_sk = int(input("Įveskite antrą skaičių: "))

    if veiksmas == '1':
        ats = (f'{pirmas_sk} + {antras_sk} = {pirmas_sk + antras_sk}')