from aineko.internals.node import AbstractNode
from typing import Optional
import secrets


class InventorySimulator(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.inventory = params.get('initial_inventory', {})

    def _execute(self, params: Optional[dict] = None) -> None:
        for item, count in self.inventory.items():
            update = secrets.choice(range(-5, 11))
            new_count = max(count + update, 0)
            self.inventory[item] = new_count
            self.producers['inventory_updates'].produce({item: new_count})
            self.log(f'Updated {item}: {count} -> {new_count}')


class InventoryLogger(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        message = self.consumers['inventory_updates'].consume()
        if message is None:
            return
        self.log(f'Inventory update received: {message}')
