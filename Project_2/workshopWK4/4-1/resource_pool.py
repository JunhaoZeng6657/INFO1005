class ResourcePool:
    MIN_RESOURCE = 0

    def __init__(
            self,
            necrotic_power=0,
            spirit_essence=0,
            bone_fragments=0,
            flesh_remains=0,
            ectoplasm=0
    ):
        self.__necrotic_power = necrotic_power
        self.__spirit_essence = spirit_essence
        self.__bone_fragments = bone_fragments
        self.__flesh_remains = flesh_remains
        self.__ectoplasm = ectoplasm

    def get_necrotic_power(self):
        return self.__necrotic_power

    def get_spirit_essence(self):
        return self.__spirit_essence

    def get_bone_fragments(self):
        return self.__bone_fragments

    def get_flesh_remains(self):
        return self.__flesh_remains

    def get_ectoplasm(self):
        return self.__ectoplasm

    necrotic_power = property(get_necrotic_power)
    spirit_essence = property(get_spirit_essence)
    bone_fragments = property(get_bone_fragments)
    flesh_remains = property(get_flesh_remains)
    ectoplasm = property(get_ectoplasm)

    def __validate_amounts(
            self,
            necrotic_power,
            spirit_essence,
            bone_fragments,
            flesh_remains,
            ectoplasm
    ):
        if not isinstance(necrotic_power,int):
            return False

        if not isinstance(spirit_essence,int):
            return False

        if not isinstance(bone_fragments,int):
            return False

        if not isinstance(flesh_remains,int):
            return False

        if not isinstance(ectoplasm,int):
            return False

        if necrotic_power < ResourcePool.MIN_RESOURCE:
            return False

        if spirit_essence < ResourcePool.MIN_RESOURCE:
            return False

        if bone_fragments < ResourcePool.MIN_RESOURCE:
            return False

        if flesh_remains < ResourcePool.MIN_RESOURCE:
            return False

        if ectoplasm < ResourcePool.MIN_RESOURCE:
            return False

        return True

    def add_resources(
            self,
            necrotic_power=0,
            spirit_essence=0,
            bone_fragments=0,
            flesh_remains=0,
            ectoplasm=0
    ):
        if not self.__validate_amounts(
                necrotic_power,
                spirit_essence,
                bone_fragments,
                flesh_remains,
                ectoplasm
        ):
            print("Invalid resource amounts.")
            return

        self.__necrotic_power += necrotic_power
        self.__spirit_essence += spirit_essence
        self.__bone_fragments += bone_fragments
        self.__flesh_remains += flesh_remains
        self.__ectoplasm += ectoplasm

    def has_resources(
            self,
            necrotic_power,
            spirit_essence,
            bone_fragments,
            flesh_remains,
            ectoplasm
    ):
        if not self.__validate_amounts(
                necrotic_power,
                spirit_essence,
                bone_fragments,
                flesh_remains,
                ectoplasm
        ):
            print("Invalid resource amounts.")
            return False

        if self.__necrotic_power < necrotic_power:
            return False

        if self.__spirit_essence < spirit_essence:
            return False

        if self.__bone_fragments < bone_fragments:
            return False

        if self.__flesh_remains < flesh_remains:
            return False

        if self.__ectoplasm < ectoplasm:
            return False

        return True

    def consume_resources(
            self,
            necrotic_power,
            spirit_essence,
            bone_fragments,
            flesh_remains,
            ectoplasm
    ):
        if not self.has_resources(
                necrotic_power,
                spirit_essence,
                bone_fragments,
                flesh_remains,
                ectoplasm
        ):
            print("Not enough resources.")
            return False
        self.__necrotic_power -= necrotic_power
        self.__spirit_essence -= spirit_essence
        self.__bone_fragments -= bone_fragments
        self.__flesh_remains -= flesh_remains
        self.__ectoplasm -= ectoplasm
        return True

    def __str__(self):
        return (
            f"Resource Pool\n"
            f"Necrotic Power: {self.__necrotic_power}\n"
            f"Spirit Essence: {self.__spirit_essence}\n"
            f"Bone Fragments: {self.__bone_fragments}\n"
            f"Flesh Remains: {self.__flesh_remains}\n"
            f"Ectoplasm: {self.__ectoplasm}"
        )
