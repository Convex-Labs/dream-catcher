from aineko.core.node import AbstractNode
from typing import Optional
import os
import json


class PartyPlannerNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize any state or configurations."""
        self.party_data_file = params.get('party_data_file', 'party_data.json')
        if not os.path.exists(self.party_data_file):
            with open(self.party_data_file, 'w') as file:
                json.dump([], file)

    def _execute(self, params: Optional[dict] = None) -> None:
        """Main logic for planning the party."""
        # Fetch new party requests
        party_request = self.consumers['party_requests'].next()
        if party_request:
            # Process the party request
            self.log(f"Received party request: {party_request}")
            # Add the party request to the party data
            with open(self.party_data_file, 'r+') as file:
                party_data = json.load(file)
                party_data.append(party_request)
                file.seek(0)
                json.dump(party_data, file)
            self.log(f"Party request added to the planner: {party_request}")
            # Produce a confirmation message
            self.producers['party_confirmations'].produce({'confirmation': 'Party successfully planned', 'details': party_request})
