class Undead:
    MIN_HEALTH = 1
    MAX_HEALTH = 100

    MIN_POWER = 1
    MAX_POWER = 50

    MAX_LEVEL = 18

    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 5

    def __init__(self,identifier,name,health,power):
        if health < Undead.MIN_HEALTH:
            health = Undead.MIN_HEALTH
        elif health > Undead.MAX_HEALTH:
            health = Undead.MAX_HEALTH

        if power < Undead.MIN_POWER:
            power = Undead.MIN_POWER
        elif power > Undead.MAX_POWER:
            power = Undead.MAX_POWER
        
        self.__identifier = identifier
        self.__name = name
        self.__health = health
        self.__power = power
        self.__level = 0

    def get_identifier(self):
        return self.__identifier

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level
    
    # Read-Only properties
    identifier = property(get_identifier)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        if self.__level >= Undead.MAX_LEVEL:
            print("Maximum level reached,")
            return
        self.__level += 1
        self.__health += Undead.HEALTH_PER_LEVEL
        self.__power += Undead.POWER_PER_LEVEL

        if self.__health > Undead.MAX_HEALTH:
            self.__health = Undead.MAX_HEALTH

        if self.__power > Undead.MAX_POWER:
            self.__power = Undead.MAX_POWER

    def __str__(self):
        return(
            f"{self.__identifier} - {self.__name},"
            f"Level:{self.__level},"
            f"Health:{self.__health}/{Undead.MAX_HEALTH},"
            f"Power:{self.__power}/{Undead.MAX_POWER}"
        )
    