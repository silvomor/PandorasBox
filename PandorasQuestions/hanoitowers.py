def TowerOfHanoi(n, fromTower, toTower, auxTower):
    if n == 1:
        print(f"move disk 1 from {fromTower} to {toTower}")
        return 

    TowerOfHanoi(n-1, fromTower, auxTower, toTower)

    print(f"move disk {n} from {fromTower} to {toTower}")

    TowerOfHanoi(n-1, auxTower, toTower, fromTower)

TowerOfHanoi(int(input("ENTER NO OF DISKS : ")), 'A', 'B', 'C')