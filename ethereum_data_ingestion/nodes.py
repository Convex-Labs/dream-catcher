from aineko.core.node import AbstractNode
from typing import Optional
import os
import psycopg2
from web3 import Web3


class EthereumDataFetcher(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize connection with Ethereum node."""
        self.web3 = Web3(Web3.HTTPProvider(params.get('ethereum_node_http')))
        if not self.web3.isConnected():
            raise ConnectionError('Unable to connect to Ethereum node.')

    def _execute(self, params: Optional[dict] = None) -> None:
        """Fetch data from Ethereum blockchain."""
        latest_block = self.web3.eth.get_block('latest')
        self.producers['ethereum_data'].produce(latest_block)


class PostgresDataInserter(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize connection with PostgreSQL database."""
        self.conn = psycopg2.connect(
            dbname=params.get('dbname'),
            user=params.get('user'),
            password=params.get('password'),
            host=params.get('host'),
            port=params.get('port')
        )
        self.cursor = self.conn.cursor()

    def _execute(self, params: Optional[dict] = None) -> None:
        """Insert data into PostgreSQL database."""
        data = self.consumers['ethereum_data'].next()
        if data:
            block_number = data['number']
            block_hash = data['hash'].hex()
            self.cursor.execute(
                'INSERT INTO ethereum_blocks (block_number, block_hash) VALUES (%s, %s)',
                (block_number, block_hash)
            )
            self.conn.commit()
