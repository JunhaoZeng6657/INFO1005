from resource_pool import ResourcePool
from undead import Undead

class SummonRitual:
    def __init__(
            self,
            ritual_name,
            undead_name,
            starting_health,
            starting_power,
            necrotic_power_cost,
            spirit_essence_cost,
            bone_fragments_cost,
            flesh_remains_cost,
            ectoplasm_cost
    ):
        self.__ritual_name = ritual_name
        self.__undead_name = undead_name
        self.__starting_health = starting_health
        self.__starting_power = starting_power
        self.__necrotic_power_cost = necrotic_power_cost
        self.__spirit_essence_cost = spirit_essence_cost
        self.__bone_fragments_cost = bone_fragments_cost
        self.__flesh_remains_cost = flesh_remains_cost
        self.__ectoplasm_cost = ectoplasm_cost

    def can_perform(self,resources):
        if not isinstance(resources, ResourcePool):
            print("Invalid resource pool.")
            return False

        return resources.has_resources(
            self.__necrotic_power_cost,
            self.__spirit_essence_cost,
            self.__bone_fragments_cost,
            self.__flesh_remains_cost,
            self.__ectoplasm_cost
        )

    def __consume_resources(self,resources):
        if not isinstance(resources, ResourcePool):
            print("Invalid resource pool.")
            return False

        resources.consume_resources(
            self.__necrotic_power_cost,
            self.__spirit_essence_cost,
            self.__bone_fragments_cost,
            self.__flesh_remains_cost,
            self.__ectoplasm_cost
        )

    def __create_undead(self,identifier):
        return Undead(
            identifier,
            name=self.__undead_name,
            health=self.__starting_health,
            power=self.__starting_power
        )

    def perform_ritual(self,resources,identifier):
        if not self.can_perform(resources):
            print("Not enough resources to perform the ritual.")
            return None

        if not self.__consume_resources(resources):
            print("Failed to consume resources.")
            return None

        return self.__create_undead(identifier)

    def __str__(self):
        return (
            f"Summon Ritual: {self.__ritual_name}\n"
            f"Undead Name: {self.__undead_name}\n"
            f"Starting Health: {self.__starting_health}\n"
            f"Starting Power: {self.__starting_power}\n"
            f"Necrotic Power Cost: {self.__necrotic_power_cost}\n"
            f"Spirit Essence Cost: {self.__spirit_essence_cost}\n"
            f"Bone Fragments Cost: {self.__bone_fragments_cost}\n"
            f"Flesh Remains Cost: {self.__flesh_remains_cost}\n"
            f"Ectoplasm Cost: {self.__ectoplasm_cost}"
        )