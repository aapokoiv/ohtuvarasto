from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Mehuvarasto: {mehua}, Olutvarasto: {olutta}")
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}, Olutvarasto: {olutta}")

    olutta.lisaa_varastoon(1000.0)
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}, Olutvarasto: {olutta}")



if __name__ == "__main__":
    main()
