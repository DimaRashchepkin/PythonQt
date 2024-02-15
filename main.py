from train import Train


def main():
    machine = Train("First", "15/02/24 15:00", "15/02/24 20:00")
    print(machine.travel_time())


if __name__ == '__main__':
    main()
