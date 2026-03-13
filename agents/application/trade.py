import shutil
from pathlib import Path

from agents.application.executor import Executor as Agent
from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.polymarket.polymarket import Polymarket


class Trader:
    def __init__(self):
        self.polymarket = Polymarket()
        self.gamma = Gamma()
        self.agent = Agent()

    def pre_trade_logic(self) -> None:
        self.clear_local_dbs()

    def clear_local_dbs(self) -> None:
        """Clear local database directories."""
        for db_dir in ["local_db_events", "local_db_markets"]:
            db_path = Path(db_dir)
            if db_path.exists():
                try:
                    shutil.rmtree(db_path)
                except OSError as e:
                    pass

    def one_best_trade(self) -> None:
        """

        one_best_trade is a strategy that evaluates all events, markets, and orderbooks

        leverages all available information sources accessible to the autonomous agent

        then executes that trade without any human intervention

        """
        try:
            self.pre_trade_logic()

            events = self.polymarket.get_all_tradeable_events()

            filtered_events = self.agent.filter_events_with_rag(events)

            markets = self.agent.map_filtered_events_to_markets(filtered_events)

            filtered_markets = self.agent.filter_markets(markets)

            if not filtered_markets:
                return

            market = filtered_markets[0]
            best_trade = self.agent.source_best_trade(market)

            amount = self.agent.format_trade_prompt_for_execution(best_trade)
            # Please refer to TOS before uncommenting: polymarket.com/tos
            # trade = self.polymarket.execute_market_order(market, amount)

        except Exception as e:
            self.one_best_trade()

    def maintain_positions(self):
        pass

    def incentive_farm(self):
        pass


if __name__ == "__main__":
    t = Trader()
    t.one_best_trade()
